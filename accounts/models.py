from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class User(AbstractBaseUser):
    full_name = models.CharField(max_length=150,unique=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    USERNAME_FIELD = 'full_name'

    REQUIRED_FIELDS = ['fullname']