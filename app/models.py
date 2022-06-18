from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    neighborhood_location = models.CharField(max_length=100)
    occupants_count = models.IntegerField()
    
    
    def create_neighborhood(self):
        self.save()
        
    def delete_neighborhodd(self):
        self.delete()
    @classmethod   
    def find_neighborhood(cls, id):
        return cls.objects.get(id=id)




class Profile(models.Model):
    image = CloudinaryField('image', null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
class Business(models.Model):
    business_image = CloudinaryField('image', null=True)
    business_name = models.CharField(max_length=100)
    business_email = models.EmailField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    
    def create_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
    
    def find_businesss(self,id):
        return Business.objects.get(id=id)
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=100)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.name} {self.neighborhood.name}"
    
    