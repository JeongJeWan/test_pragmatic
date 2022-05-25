from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    people = models.CharField(max_length=200, null=True)
    extinguisher = models.CharField(max_length=200, null=True)
    water = models.CharField(max_length=200, null=True)
    fire = models.CharField(max_length=200, null=True)
    crack = models.CharField(max_length=200, null=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
