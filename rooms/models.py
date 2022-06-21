from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from users.models import User

# Create your models here.



class AbstractItem(core_models.TimeStampModel):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True



# for many to many relatioship
class RoomType(AbstractItem):
     class Meta:
        verbose_name='Room Type'

class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural='Amenties'

class HouseRule(AbstractItem):
     class Meta:
        verbose_name='House Rule'

class Facility(AbstractItem):
     class Meta:
        verbose_name_plural='Facilities'

class Photo(core_models.TimeStampModel):
    caption=models.CharField(max_length=250, blank=True, null=True)
    file=models.ImageField(upload_to='rooms')
    room= models.ForeignKey("Room", on_delete=models.CASCADE, related_name='photos')
    def __str__(self) -> str:
        return  self.caption
    


class Room(core_models.TimeStampModel):

    """Room model Defination"""
    name = models.CharField(max_length=250)
    
    country = CountryField()
    description = models.TextField()
    city = models.CharField(max_length=250)
    price = models.IntegerField()
    address = models.CharField(max_length=250)
    beds = models.IntegerField()
    bath = models.IntegerField()
    bedrooms = models.IntegerField()
    guest = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instan_book = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE,related_name='rooms' )
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, related_name='rooms')
    amenties= models.ManyToManyField(Amenity, blank=True,related_name='rooms' )
    houseRules=models.ManyToManyField(HouseRule, blank=True, related_name='rooms')
    facilities=models.ManyToManyField(Facility, blank=True, related_name='rooms')

    def __str__(self) -> str:
        return self.name
    
    def save(self,*args, **kwargs):
        self.city=str.capitalize(self.city)
        super().save(*args, **kwargs)
    
    
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
    
    
    
    def total_rating(self):
        all_reviews=self.reviews.all()
        all_rating=0
        if len(all_reviews)> 0:
            for review in all_reviews:
                all_rating +=review.rating_average()
            return all_rating/len(all_reviews)
        return 0
            
