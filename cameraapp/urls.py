from django.urls import path
from . import views

app_name = 'cameraapp'

urlpatterns = [
    path('', views.index, name='camera_main'),
    path('list/', views.list_index, name='list'),
]
