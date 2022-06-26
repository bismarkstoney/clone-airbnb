import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
# Create your models here.


class User(AbstractUser):

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_CHINESE = 'ch'
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_CHINESE, 'Chinese')
    )

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_ORDER = 'other'
    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
        (GENDER_ORDER, 'Other '),
    )

    CURRENCY_USD = 'usd'
    CURRENCY_RMB = 'rmb'
    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_RMB, 'RMB')
    )

    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to=('avatars'))
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, blank=True, max_length=50)
    currency = models.CharField(
        max_length=5, choices=CURRENCY_CHOICES, blank=True)
    supperhost = models.BooleanField(default=False)
    email_verified=models.BooleanField(default=False)
    email_secret=models.CharField(max_length=120, default="", blank=True)
    
    
    def verify_email(self):
        if self.email_verified is False:
            secret=uuid.uuid4().hex[:20]
            self.email_secret=secret
            send_mail('Verify Fie account', 'Verify account', 'd764f096d41192', [self.email], fail_silently=False)
        return 
    
