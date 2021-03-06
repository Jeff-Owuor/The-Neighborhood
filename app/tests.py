from django.test import TestCase
from . models import Post,Profile,Neighborhood,Business


class TestModels(TestCase):
    def setup(self):
        Post.objects.create(id=1,title='Test',post='https://cloudinaryimage.com',description='This is basically a test',hood_id=1,user_id=1)
        Profile.objects.create(id=1,image='https://imagetocloudinary.com',neighborhood_id=1,user_id=1)
        Business.objects.create(id=1,image='https://imagetocloudinary.com',name='test',email='party@gmail.com',neighborhood_id=1,user_id=1)
        Neighborhood.objects.create(id=1,neighborhood_name='thc',neighborhood_location='Kasarani',occupants_count=2)
        
    def test_post_instance(self):
        post = Post.objects.get(id=1)
        self.assertTrue(isinstance(post,Post))
        
    def test_profile_instance(self):
        profile = Profile.objects.get(id=1)
        self.assertTrue(isinstance(profile,Profile))
        
    def test_business_instance(self):
        business = Business.objects.get(id=1)
        self.assertTrue(isinstance(business,Business))
        
    def test_neighborhood_instance(self):
        neighborhood = Neighborhood.objects.get(id=1)
        self.assertTrue(isinstance(neighborhood,Neighborhood))
        
    def test_save_post(self):
        post = Post.objects.get(id=1)
        post.create_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)
    
    def test_save_business(self):
        business_post = Business.objects.get(id=1)
        business_post.create_business()
        business_posts = Business.objects.all()
        self.assertTrue(len(business_posts) > 0)
        
    def test_save_neighborhood(self):
        hood = Neighborhood.objects.get(id=1)
        hood.create_neighborhood()
        hoods= Business.objects.all()
        self.assertTrue(len(hoods) > 0)
        
    def test_search_business(self):
        business = Business.objects.get(id=1)
        business.create_business()
        post = Business.search_project('Gym equipment')
        self.assertTrue(len(post) > 0)
        
    def test_delete_business(self):
        business = Business.objects.get(id=1)
        business.create_business()
        post = Business.delete_business()
        self.assertTrue(len(post) == 0)
    
    def test_delete_post(self):
        post = Post.objects.get(id=1)
        post.create_post()
        posts =Post.delete_post()
        self.assertTrue(len(posts) == 0)
        
    def test_delete_neighborhood(self):
        hood = Neighborhood.objects.get(id=1)
        hood.create_post()
        hood_posts =Neighborhood.delete_neighborhood()
        self.assertTrue(len(hood_posts) == 0)

        
        
        


# Create your tests here.
