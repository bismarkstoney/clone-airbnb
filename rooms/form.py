from email.policy import default
from django import forms
from .models import Amenity, RoomType, Facility, HouseRule
from django_countries.fields import CountryField



class Form(forms.Form):
    city=forms.CharField()
    price=forms.IntegerField(required=False)
    room_type=forms.ModelChoiceField(queryset=RoomType.objects.all(), required=False, empty_label='Any kind')
    country=CountryField(default='GH').formfield()
    guest= forms.IntegerField(required=False)
    bedrooms=forms.IntegerField(required=False)
    beds=forms.IntegerField(required=False)
    bath=forms.IntegerField(required=False)
    instant_book=forms.BooleanField(required=False)
    amenties= forms.ModelMultipleChoiceField(queryset=Amenity.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    facilities= forms.ModelMultipleChoiceField(queryset=Facility.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    house_rules= forms.ModelMultipleChoiceField(queryset=HouseRule.objects.all(), widget=forms.CheckboxSelectMultiple,required=False )
    
    
    
    
    