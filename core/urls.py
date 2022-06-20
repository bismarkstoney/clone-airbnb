from django.urls import path
from .views import all_rooms

app_name = 'core'



urlpatterns = [
    path('', all_rooms)
]