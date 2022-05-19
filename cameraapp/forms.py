from django.forms import ModelForm

from .models import Camera


class Camera_form(ModelForm):

    class Meta:
        model = Camera
        fields = ['caption', 'camera']