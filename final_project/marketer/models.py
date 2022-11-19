from django.db import models
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.



class Request (models.Model):
    title = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024)
    description = models.TextField()
    #publish_date = models.DateTimeField()
    #is_closed = models.BooleanField()
    image = models.ImageField(upload_to="images/")




class Offer(models.Model):
  requestt = models.ForeignKey(Request, on_delete = models.CASCADE) 
  name = models.CharField(max_length=256)
  content = models.TextField()
 # created_at = models.DateTimeField(auto_now=True)
  #amount = models.CharField(max_length=256)





#creating a profile for the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    age = models.IntegerField()
    address = models.CharField(max_length=2048)


class Contact (models.Model):

  name = models.CharField(max_length=256)
  email = models.CharField(max_length=256)
  subject = models.CharField(max_length=650)
  message = models.CharField(max_length=1000)


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

   

