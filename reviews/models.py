from django.db import models
from core.models import TimeStampModel
# Create your models here.

class Review(TimeStampModel):
    """Review Modal defination"""
    review = models.TextField()
    accuracy=models.IntegerField() 
    communication=models.IntegerField() 
    cleanliness=models.IntegerField() 
    location=models.IntegerField()  
    check_in=models.IntegerField()   
    value=models.IntegerField()  
    user=models.ForeignKey("users.User",  on_delete=models.CASCADE) 
    room=models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name='reviews')  
    
    
    
    def __str__(self) -> str:
        return f'{self.review} - {self.room}'
    
    def rating_average(self):
        avg=(self.accuracy + self.communication + self.cleanliness 
             + self.location + self.check_in + self.value)/6
        return round(avg,2)
    