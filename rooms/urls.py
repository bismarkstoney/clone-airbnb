from django.urls import path, re_path
from core.views import room_detail

app_name='rooms'


urlpatterns = [
    path('<int:pk>/',room_detail, name='detail' )
]