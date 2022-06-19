from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display=('__str__','check_in', 'check_out', 'guest', 'status' , 'processing')
