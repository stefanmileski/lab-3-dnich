from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Anonymous')


class File(models.Model):
    file = models.FileField(upload_to='path/to/uploads/')


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    files = models.ManyToManyField(File)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)


class Blocklist(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    blocked_users = models.ManyToManyField(MyUser, related_name='blocked_by')


class Comment(models.Model):
    post = models.ManyToManyField(Post, related_name='comments')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
