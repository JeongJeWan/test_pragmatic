from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article
from mapapp.models import Map


class Comment(models.Model):
    map = models.ForeignKey(Map, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
