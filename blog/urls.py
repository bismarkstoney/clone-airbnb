from django.urls import path, re_path
from .views import BlogView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='home')
]