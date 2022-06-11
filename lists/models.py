from django.db import models
from core.models import TimeStampModel
# Create your models here.

class List(TimeStampModel):
    """List Model Defination"""
    
    name=models.CharField(max_length=50)
    user=models.ForeignKey("users.User",on_delete=models.CASCADE)
    rooms=models.ManyToManyField("rooms.Room", blank=True)
    
    def __str__(self) -> str:
        return self.name