from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, AbstractUser
)

# Create your models here.

''' For Storing Basic User Information ''' 

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255,unique=True,blank=False)
    email = models.EmailField(max_length=255)
    aadhar_no = models.CharField(max_length=255,default=None)
    address = models.TextField(blank=False)
    category = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['first_name','last_name','username',
                        'aadhar_no','address','email','is_admin','category','password']

    USERNAME_FIELD = 'phone'


    def get_username(self):
        return self.phone

