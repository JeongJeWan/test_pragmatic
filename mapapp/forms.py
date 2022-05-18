from django.forms import ModelForm
from django import forms

from mapapp.models import Map
from projectapp.models import Project


class MapCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto; text-align: left;'}))

    class Meta:
        model = Map
        fields = ['title', 'image', 'content']