from django.urls import path

from profileapp.views import ProfileCreateViews, ProfileUpdateView

app_name = "profileapp"

urlpatterns = [
    path('create/', ProfileCreateViews.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]
