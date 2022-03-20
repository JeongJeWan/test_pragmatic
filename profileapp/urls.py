from django.urls import path

from profileapp.views import ProfileCreateViews

app_name = "profileapp"

urlpatterns = [
    path('create/', ProfileCreateViews.as_view(), name='create'),
]
