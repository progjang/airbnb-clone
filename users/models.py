from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    
    """ Custom User Model """

    GENDER_MALE = "mail"
    GENDER_FEMALE = "femail"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "EN"
    LANGUAGE_KOREAN = "KR"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KRW"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw"),
    )

    avatar = models.ImageField(upload_to="avatar", blank=True)
    gender = models.CharField(
        choices= GENDER_CHOICES, max_length=10, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True
    )
    superhost = models.BooleanField(default=False)
    
     
