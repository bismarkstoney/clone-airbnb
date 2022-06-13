from pyexpat import model
from django.contrib import admin
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
    
    
    

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomType, Amenity, Facility,HouseRule )
class ItemAdmin(admin.ModelAdmin):
  
    def used_by(self,obj):
        return obj.rooms.count()
    list_display=('name','used_by')