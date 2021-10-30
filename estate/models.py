import sys
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.urls import reverse
# Create your models here.

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,null=True)
    occupant_count = models.IntegerField(null=True)
    
    def save_neighborhood(self):
        self.save()
        
    @classmethod
    def delete_neighborhood(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_neighborhood(cls,id,new_name):
        cls.objects.filter(id=id).update(hood_name = 'newname')
   
    @classmethod
    def update_family_count(cls,id,new_occupant):
       cls.objects.filter(id=id).update(family_size = new_occupant) 

    @classmethod
    def search_hood(cls,id):
       search= cls.objects.filter(neighborhood_name__icontains=id)
       return search
    
    
   
class Business(models.Model):
    name=models.CharField(max_length=100)
    business_owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    email=models.EmailField()
    business_image= CloudinaryField('business', null=True)
    business_location=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    location=models.CharField(max_length=225,null=True,blank=True)

    def save_business(self):
        self.save()
    
    @classmethod
    def delete_business(id,cls):
        cls.objects.filter(id).delete()
    
    @classmethod
    def update_business(cls,id,new_name):
        cls.objects.filter(id=id).update(new_business=new_name)
    
    @classmethod
    def search_business(cls,id):
        business = cls.objects.filter(name__icontains = id)
        return business

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('business-detail',kwargs={'pk':self.pk})

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = TextField(null=True)
    date_posted = models.DateTimeField(auto_now=True)
    neighourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True,blank=True)

    
    def get_absolute_url(self):
        return reverse('post')
    
