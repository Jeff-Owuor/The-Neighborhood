from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse


class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    neighborhood_location = models.CharField(max_length=100)
    health_tell = models.BigIntegerField(null=True, blank=True)
    police_number = models.BigIntegerField(null=True, blank=True)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    
    
    def create_neighborhood(self):
        self.save()
        
    def delete_neighborhodd(self):
        self.delete()
    @classmethod   
    def find_neighborhood(cls, id):
        return cls.objects.get(id=id)
    


class Profile(models.Model):
    image = CloudinaryField('image', null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True,blank=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('index')


class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = CloudinaryField('image', null=True)
    description = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hood_post') 
    
    def create_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()
    
    def find_post(self,id):
        return Post.objects.get(id=id)
    
class Business(models.Model):
    image = CloudinaryField('image', null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    
    def create_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
    
    def find_businesss(self,id):
        return Business.objects.get(id=id)
    
    def __str__(self):
        return self.name
    
    