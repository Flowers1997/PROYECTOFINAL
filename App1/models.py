from email.policy import default
from typing import TextIO
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    post_body = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image_up = models.ImageField(upload_to='images/',blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now
        self.save
        
    def __str__(self):
        return self.title
   

 
class MemberUser(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='User')
    web=models.URLField(null=True,blank=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        
        return self.user.username


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    avatar= models.ImageField(upload_to='avatar', null=True, blank=True, default='media\avatar\avatarDefault.png')

class Mensaje(models.Model):
    cuerpo=models.CharField(max_length=150)
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Emisor')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Receptor')
    enviado = models.DateTimeField(auto_now_add=True)
    leido=models.BooleanField(default=False)