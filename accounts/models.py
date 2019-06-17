from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('You need a valid email address')
        if not password:
            raise ValueError('Incorrect Password')

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
    
    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,password=password,is_staff=True
        )
        return user
    
    def create_superuser(self, email, password=None):
         user = self.create_user(
            email,password=password,is_staff=True,is_admin=True
        )



class User(AbstractBaseUser):
    full_name = models.CharField(max_length=150,unique=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'full_name'

    REQUIRED_FIELDS = ['fullname']

    def get_username(self):
        return self.full_name

    def __str__(self):
        return self.full_name