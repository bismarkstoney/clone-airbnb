from pyexpat import model
from django.contrib import admin
from .models import Room, RoomType, Facility, Amenity, HouseRule, Photo
# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomType, Amenity, Facility,HouseRule )
class ItemAdmin(admin.ModelAdmin):
    pass
