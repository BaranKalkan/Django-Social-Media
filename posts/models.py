import datetime
from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
     
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_pic = models.CharField(max_length=50)


class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    media_path = models.CharField(max_length=200)
    media_desc = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('date published')
    likes = models.ManyToManyField(CustomUser, related_name="likes", through='PostLikes')
    
    def __str__(self):
        return self.media_path
 
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
        
    def __str__(self):
        return self.comment_text

class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



