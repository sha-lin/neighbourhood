from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.fields import TextField
from estate.models import Neighborhood

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = CloudinaryField('profile-photo',null=True, transformation=[{'width':300, 'height':300}])
    bio = models.TextField(null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'