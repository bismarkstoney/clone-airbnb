from django.urls import path, re_path
from .views import all_rooms



urlpatterns = [
    path('/rooms',all_rooms, name='home' )
]