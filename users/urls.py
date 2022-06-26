from django.urls import path, re_path
from .views import Login, log_out,Sigup

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout', log_out, name='logout'),
    path('sigup',Sigup.as_view(), name='signup' )
         
]