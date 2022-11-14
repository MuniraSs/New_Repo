from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class request(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField()
    publish_date = models.DateTimeField()
    is_published = models.BooleanField()

class offer():
    request = models.ForeignKey(request, on_delete = models.CASCADE) 
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    amount = models.CharField(max_length=256)

#creating a profile for the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    age = models.IntegerField()
    address = models.CharField(max_length=2048)
   

