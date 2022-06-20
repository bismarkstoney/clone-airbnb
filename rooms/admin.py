from pyexpat import model
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Room, RoomType, Facility, Amenity, HouseRule, Photo
# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Basic Info', {
            "fields": (
                'name','country','city' ,'price','address'
            ),
           
        }),
        
        ('Times', {
            "fields": (
                 'check_in',
                    'check_out',
                    'instan_book'
            ),
           
        }),
         ('Spaces', {
            "fields": (
                 'guest', 'beds', 'bath'
            ),
           
        }),
         
          ('Last Details', {
            "fields": (
                 'host', 
            ),
           
        }),
        
         ('More About the Space ', {
            'classes': ('collapse',),
            "fields": (
               
                 'amenties', 'facilities', 'houseRules'
            ),
           
        }),
         
         
        

    )
    
    list_display= ('name','country','city' ,'price','address','beds',
                    'bath',
                    'bedrooms',
                    'guest',
                    'check_in',
                    'check_out',
                    'instan_book', 'count_amenties','total_rating')
    list_filter=('instan_book',)
    search_fields=('city', )
    filter_horizontal=('amenties', 'facilities', 'houseRules')
    
    def count_amenties(self, obj):
        return obj.amenties.count()
    
    # def save_model(self, request, obj, form, change):
    #     print(obj, change, form)
    #     return super().save_model(request, obj, form, change)
    
    
    

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=('caption', 'room', '__str__', 'get_thumnail')
    
    def get_thumnail(self,obj):
        return mark_safe(f'<img width="50px" height="50px" src="{obj.file.url}"/>')

@admin.register(RoomType, Amenity, Facility,HouseRule )
class ItemAdmin(admin.ModelAdmin):
  
    def used_by(self,obj):
        return obj.rooms.count()
    list_display=('name','used_by')