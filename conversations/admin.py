from django.contrib import admin
from .models import Message, Conversation


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    pass

@admin.register(Conversation)
class AdminConversation(admin.ModelAdmin):
    pass