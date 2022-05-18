from django.urls import path

from mapapp.views import MapCreateView, MapDetailView, MapListView, MapUpdateView, MapDeleteView

app_name = 'mapapp'

urlpatterns = [
    path('list/', MapListView.as_view(), name='list'),

    path('create/', MapCreateView.as_view(), name='create'),
    path('detail/<int:pk>', MapDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MapUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MapDeleteView.as_view(), name='delete'),
]