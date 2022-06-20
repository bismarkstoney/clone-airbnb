from django.contrib import admin
from .models import Message, Conversation


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    
    """Conversation Admin Defination"""
    list_display=("__str__",)
    
    

@admin.register(Conversation)
class AdminConversation(admin.ModelAdmin):
    
    """Conversation Admin Defination"""
    list_display=("__str__",'count_message', 'count_participants')
    
   
    