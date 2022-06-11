from re import L
from django.contrib import admin
from .models import List
# Register your models here.

@admin.register(List)
class AdminList(admin.ModelAdmin):
    pass