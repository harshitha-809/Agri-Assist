from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    usertype = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    mobile = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    soilType = models.CharField(max_length=50, null=True, blank=True)
    primaryCrops = models.CharField(max_length=100, null=True, blank=True)
    ownership = models.CharField(max_length=50, null=True, blank=True)
    businessType = models.CharField(max_length=50, null=True, blank=True)
    primaryPurpose = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    uname = models.CharField(max_length=20)
    email = models.EmailField(_("email address"), unique=True)
    # password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['usertype','name','dob','mobile','gender','nationality','town','state','pincode','uname',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email