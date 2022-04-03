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

    def create_patient(self, email,active, name,telecom,gender,birthDate,decreased,address,maritalStatus,contact, communication,managingOrganization,link, password = None):
        if email is None:
            raise TypeError('Users must have an email address')
        patient = Patient(email=self.normalize_email(email),active=active, name=name,
                          telecom=telecom,gender=gender,birthDate=birthDate,
                          decreased=decreased,address=address,maritalStatus=maritalStatus,
                          contact=contact, communication=communication,
                          managingOrganization=managingOrganization,link=link, 
                          occupation=occupation)
        patient.set_password(password)
        patient.save()
        return patient

class PractitionerManager(BaseUserManager):
    
    def create_practitioner(self, active, name,email, telecom, address, gender, birthDate, qualification, communication, password = None):
        if email is None:
            raise TypeError('Users must have an email address.')
        doctor = Practitioner(active=active, name=name, email=self.normalize_email(email), telecom=telecom, address=address, gender=gender, birthDate=birthDate, qualification=qualification, communication=communication)
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

class Patient(models.Model):
    GENDER_CODE = (
        ("1","male"),
        ("2","female"),
        ("3","other"),
        ("4","unknown")
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="patient")
    active = models.BooleanField(db_index=True)
    email = models.EmailField(db_index=True, unique=True)
    
    # name
    # telecom
    gender = models.CharField(db_index=True, max_length=100, choices = GENDER_CODE)
    birthDate = models.DateField(db_index=True)
    # deceased
    # address
    # maritalStatus
    #TODO: --> multipleBirth
    #TODO: --> photo
    # contact
    # communication 
    # TODO:--> generalPractitioner
    # managingOrganization
    # link
 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['active', 'email','name','telecom','gender','birthDate','decreased','address','maritalStatus','contact', 'communication','managingOrganization','link']

    objects = PatientManager()

    def __str__(self):
        return self.email

class Practitioner(models.Model):
    GENDER_CODE = (
        ("1","male"),
        ("2","female"),
        ("3","other"),
        ("4","unknown")
    )
    #identifier
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="practitioner")
    active = models.BooleanField(db_index=True, max_length=100,null=True, blank=True)
    # name 
    # telecom
    # address
    gender = models.CharField(db_index=True, max_length=100, choices = GENDER_CODE)
    birthDate = models.DateField(db_index=True)
    # photo
    # qualification
    # communication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'hospital_name']

    objects = PractitionerManager()

    def __str__(self):
        return self.first_name
