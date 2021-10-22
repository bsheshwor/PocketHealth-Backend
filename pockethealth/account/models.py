import time
import datetime
import jwt

from datetime import timedelta

from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """Helps django work with our custom user model."""

    def create_user(self, first_name,last_name, email, password=None):
        """Creates a new user profile object"""

        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, first_name,last_name, email,password):
        """Creates and saves a new superuser with given details"""

        user = self.create_user(first_name,last_name,email, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db) 
    

    
class CustomerManager(BaseUserManager):

    def create_customer(self, first_name, last_name, email, occupation, password = None):
        if email is None:
            raise TypeError('Users must have an email address')
        customer = Customer(first_name= first_name, last_name=last_name, email = self.normalize_email(email), occupation=occupation)
        customer.set_password(password)
        customer.save()
        return customer

class DoctorManager(BaseUserManager):
    
    def create_doctor(self, first_name, last_name, email, hospital_name, password = None):
        if email is None:
            raise TypeError('Users must have an email address.')
        doctor = Doctor(first_name=first_name, last_name=last_name, email=self.normalize_email(email), hospital_name=hospital_name)
        doctor.set_password(password)
        doctor.save()
        return doctor

class User(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile inside our system"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    @property
    def token(self):
        dt = datetime.datetime.now()+timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%Y%m%d%H%M%s'))
        }, settings.SECRET_KEY, algorithm="HS256")
        
        return token
        # .decode('utf-8') 

    def get_full_name(self):
        """Used to get a users full name."""

        return (self.first_name+''+self.last_name)

    def get_short_name(self):
        """Used to get a users short name."""

        return self.first_name
    

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email

class Customer(User, PermissionsMixin):
    # user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="customer_account")
    occupation = models.CharField(db_index=True, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','occupation' ]

    objects = CustomerManager()

    def __str__(self):
        return self.first_name

class Doctor(User, PermissionsMixin):
    # user = models.OneToOneField(UserProfile,on_delete=models.CASCADE, related_name="doctor_account")
    hospital_name = models.CharField(db_index=True, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'hospital_name']

    objects = DoctorManager()

    def __str__(self):
        return self.first_name

