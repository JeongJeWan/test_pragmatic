from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Map(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='map', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='map/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)






