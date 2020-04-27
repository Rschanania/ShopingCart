from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.FileField(upload_to='user/',null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
   
    objects = models.Manager
    def __str__(self):
        return self.user.username

# Create your models here.
