from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


@admin.register(User)
class CustomeUserAdmin(UserAdmin):
    """Custome User Admin"""
    fieldsets = UserAdmin.fieldsets + (
        ('User Profile', {
            "fields": (
                "avatar", 'currency', 'language', 'supperhost', 'gender', 'bio', 'birthdate'
            ),
        }),
    )

    list_display = ('username', 'currency', 'language', 'supperhost', 'gender')
    list_filter = ('supperhost', 'language')
