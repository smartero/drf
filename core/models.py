from django.db import models
from django.contrib.auth..models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(blank=True, null=True)
    friends = models.ManyToManyField('self')
    followers = models.ManyToManyField('self', symmetrical=False)
    about = models.TextField(max_length=200, blank=True, null=True)
    full_name = models.TextField(max_length=50)
    prizes = models.TextField(max_length=300, blank=True, null=True)
    relatives = models.ManyToManyField('self')

def Posts(models.Model):
    title = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = 
    comments = 
    likes = 
    image = 
