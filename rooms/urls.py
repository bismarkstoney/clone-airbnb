from django.urls import path, re_path
from .views import  HomeView, Room_Detail, search

app_name='rooms'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>',Room_Detail.as_view(), name='detail' ),
    path('search/',search, name='search' )
]