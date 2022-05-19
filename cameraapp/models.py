from django.db import models

# Create your models here.


class Camera(models.Model):
    caption = models.CharField(max_length=100)
    camera = models.FileField(upload_to="camera/%y")

    def __str__(self):
        return self.caption
