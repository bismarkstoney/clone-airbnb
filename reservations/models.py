from django.db import models
from core.models import TimeStampModel
# Create your models here.


class Reservation(TimeStampModel):
    
    
    """Reservation Model Defination"""
    STATUS_PENDING='pending'
    STATUS_CONFIRM='confirmed'
    STATUS_CANCELLED= 'cancelled'
    
    
    STATUS_CHOICES=(
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRM, 'Confirmed'),
        (STATUS_CANCELLED, 'Cancelled')
    )
    
    status=models.CharField(max_length = 25, choices=STATUS_CHOICES, default=STATUS_PENDING)
    guest= models.ForeignKey("users.User",  on_delete=models.CASCADE)
    room= models.ForeignKey("rooms.Room",  on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    
    def __str__(self) -> str:
        return f'{self.room} - {self.check_in}'
    