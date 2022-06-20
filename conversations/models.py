from django.db import models
from core.models import TimeStampModel
# Create your models here.
class Conversation(TimeStampModel):
    participants= models.ManyToManyField("users.User",blank=True)
    
    def __str__(self) -> str:
        usernames=[]
        for user in self.participants.all():
            usernames.append(user.username)
        return " ".join(usernames)
    
    def count_message(self):
        return self.message.count()
    
    def count_participants(self):
        return self.participants.count()

class Message(TimeStampModel):
    message= models.TextField()
    user=models.ForeignKey("users.User",  on_delete=models.CASCADE)
    conversation=models.ForeignKey("conversations.Conversation", on_delete=models.CASCADE, related_name='message')
    
    def __str__(self) -> str:
        return f'{self.user}  says: {self.message}'