import time
import datetime
from unittest.util import _MAX_LENGTH
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
    

    
class PatientManager(BaseUserManager):

    def create_patient(self,email,password = None):
        if email is None:
            raise TypeError('Users must have an email address')
        patient = Patient(email = self.normalize_email(email))
        patient.set_password(password)
        patient.save()
        return patient

class PractitionerManager(BaseUserManager):
    
    def create_practitioner(self, email, password = None):
        if email is None:
            raise TypeError('Users must have an email address.')
        doctor = Practitioner(email=self.normalize_email(email))
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

class Patient(User, PermissionsMixin):
    # user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="customer_account")
    USERNAME_FIELD = 'email'
    objects = PatientManager()

    def __str__(self):
        return self.email

class PatientRegisterModel(models.Model):
    GENDER_CODE = (
        ("1","male"),
        ("2","female"),
        ("3","other"),
        ("4","unknown")
    )

    patient = models.OneToOneField(Patient,related_name = 'patient', on_delete=models.CASCADE,null=True, blank=True )
    #identifier
    active = models.BooleanField(null=True, blank=True)
    #name
    #telecom
    gender = models.CharField(max_length=225, choices = GENDER_CODE,null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    #deceased
    #address
    #maritalStatus
    #photo
    #contact
    #communication
    #TODO: generalPractitioner
    #managingOrganization
    #link

class Practitioner(User, PermissionsMixin):
    # user = models.OneToOneField(UserProfile,on_delete=models.CASCADE, related_name="doctor_account")
    USERNAME_FIELD = 'email'
    objects = PractitionerManager()

    def __str__(self):
        return self.email

class PractitionerRegisterModel(models.Model):
    GENDER_CODE = (
        ("1","male"),
        ("2","female"),
        ("3","other"),
        ("4","unknown")
    )
    practitioner = models.OneToOneField(Practitioner,related_name = 'practitioner', on_delete=models.CASCADE,null=True, blank=True )
    #identifier
    active = models.BooleanField(null=True, blank=True)
    # name
    # telecom
    # address
    gender = models.CharField(max_length=225, choices = GENDER_CODE,null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    # photo
    # qualification
    # communication

