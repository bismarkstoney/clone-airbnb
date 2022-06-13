from django.db import models
from core.models import TimeStampModel
# Create your models here.
class Conversation(TimeStampModel):
    participants= models.ManyToManyField("users.User",blank=True)
    
    def __str__(self) -> str:
        return str(self.created_at)

class Message(TimeStampModel):
    message= models.TextField()
    user=models.ForeignKey("users.User",  on_delete=models.CASCADE)
    conversation=models.ForeignKey("conversations.Conversation", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user}  says: {self.message}'