from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from .managers import CustomerUserManager

class User(AbstractUser):
    email = models.EmailField(
        max_length=150,
        unique= True,
        error_messages={
            "unique": "The email must be unique"
        }    
    )

    profile_image= models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_images",
    )

    REQUIRED_FIELDS= ["email"]
    objects= CustomerUserManager
    def __str__(self):
        return self.username
    