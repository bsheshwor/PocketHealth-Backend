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
    hospital_name = models.CharField(db_index=True, max_length=100,null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'hospital_name']

    objects = DoctorManager()

    def __str__(self):
        return self.first_name

class Period(models.Model):
    """
    This function is used to return the range of datetime.
    It is not same as duration.
    inputs:
        start: start datetime of certain period.
        end: end datetime of certain period.

    return: range(start:end)
    """
    user = models.ForeignKey(Customer,on_delete= models.CASCADE),
    start = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    end = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)

class ContactPoint(models.Model):
    """
    This function is used to return the contactPoint.

    inputs:
        SYSTEM_CHOICES: (tuple) phone | fax | email | pager | url | sms | other
        CODE: (tuple) home | work | temp | old | mobile (choices).
        HIGHEST_PRIORITY: (tuple) highest priority choices
        system: (code)(string) selecting system_choices. 
        value_mobile: (string) The actual contact point details of mobile choosen from CODE.
        value_work: (string) The actual contact point details of work choosen from CODE.
        value_home: (string) The actual contact point details of home choosen from CODE.
        rank: (positiveInt) Specify preferred order of use (1 = highest)
        period: (Period) range(start:end) datetime

    return: (dict) jsonify(CODE, HIGHEST_PRIORITY, system, value1, value2, value3, rank, period)
    """

    phone = "1"
    fax = "2"
    email = "3"
    pager = "4"
    url = "5"
    sms = "6"

    SYSTEM_CHOICES = ((phone,"phone"),
                      (fax,"fax"),
                      (email,"email"),
                      (pager,"pager"),
                      (url,"url"),
                      (sms,"sms"))

 
    USE_CODE = (
        ("1", "Mobile"),
        ("2", "Work"),
        ("3", "Home"),
        ("4", "Other")
    )

    user = models.ForeignKey(Customer,on_delete= models.CASCADE)

    system = models.CharField(max_length=20, choices= SYSTEM_CHOICES,null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    use = models.CharField(max_length=255, choices = USE_CODE, null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    period = models.OneToOneField(Period,on_delete=models.CASCADE,null=True, blank=True)

class Deceased(models.Model):
    """
    Indicates if the individual is deceased or not
    """

    user = models.ForeignKey(Customer,on_delete= models.CASCADE)
    deceasedBoolean = models.BooleanField()
    # deceasedDateTime = models.BooleanField()


class Address(models.Model):
    """
    An address for the individual.
    user(code)-->ADDRESS_CHOICES
    """
    home = "1"
    work = "2"
    temp = "3"
    billing = "4"
    # use(code)
    ADDRESS_USE_CHOICES = ((home,"Home"),
                       (work,"Work"),
                       (temp,"Temporary"),
                       (billing,"Billing"))
    
    # type(code)
    postal = "1"
    physical = "2"
    both = "3"
    ADDRESS_TYPE_CHOICES = ((postal,"Postal"),
                            (physical,"Physical"),
                            (both,"Postal & Physical"))

    #TODO: text--> appending, city and district int he form of options.
    user = models.ForeignKey(Customer,on_delete= models.CASCADE)
    use = models.CharField(max_length=225, choices = ADDRESS_USE_CHOICES,null=True, blank=True)
    address_type = models.CharField(max_length=40, choices= ADDRESS_TYPE_CHOICES,null=True, blank=True)
    text = models.CharField(max_length=500,null=True, blank=True)
    line = models.CharField(max_length=225,null=True, blank=True)
    city = models.CharField(max_length=225,null=True, blank=True)
    district = models.CharField(max_length=225,null=True, blank=True)
    state = models.CharField(max_length=225,null=True, blank=True)
    postalCode = models.CharField(max_length=225,null=True, blank=True)
    country = models.CharField(max_length=225,null=True, blank=True)
    period = models.OneToOneField(Period, on_delete= models.CASCADE)

class HumanName(models.Model):
    """
    use(code) --> usual | official | temp | nickname | anonymous | old | maiden
    """
    USE_CODE = (
        ("1","usual"),
        ("2","official"),
        ("3","temp"),
        ("4", "nickname"),
        ("5","anonymous"),
        ("6","old"),
        ("7","maiden")
    )
    user = models.ForeignKey(Customer,on_delete= models.CASCADE)
    use = models.CharField(max_length=225, choices=USE_CODE, default="2",null=True, blank=True)
    text = models.CharField(max_length=225,null=True, blank=True)
    family = models.CharField(max_length=225,null=True, blank=True)
    given = models.CharField(max_length=225,null=True, blank=True)
    prefix = models.CharField(max_length=10,null=True, blank=True)
    suffix = models.CharField(max_length= 225,null=True, blank=True)
    period = models.OneToOneField(Period,on_delete=models.CASCADE)

class MaritalStatus(models.Model):
    # coding(Coding)
    MARRIAGE_CODING = (("A", "Annulled"),
                       ("D", "Divorced"),
                       ("I","Interlocutory"),
                       ("L","Legally Separated"),
                       ("M","Married"),
                       ("P","Polygamous"),
                       ("S","Never Married"),
                       ("T","Domestic partner"),
                       ("U","unmarried"),
                       ("W","Widowed"),
                       ("UNK","unknown")
                       )
    
    user = models.ForeignKey(Customer,on_delete= models.CASCADE)
    code = models.CharField(max_length=15,null=True, blank=True)               
    text = models.CharField(max_length=255, choices = MARRIAGE_CODING,null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.text != None:
            for element in self.MARRIAGE_CODING:
                if element[1] == self.text:
                    self.code = element[0]            
        super(MaritalStatus, self).save(*args, **kwargs)



class Contact(models.Model):
    """
    All codes from system http://terminology.hl7.org/CodeSystem/v2-0131
    """
    RELATIONSHIP_CODE = (
        ("C","Emergency Contact"),	
        ("E","Employer"),	
        ("F","Federal Agency"),	
        ("I","Insurance Company"),	
        ("N","Next-of-Kin"),	
        ("S","State Agency"),	
        ("U","Unknown")
    )

    GENDER_CODE = (
        ("1","male"),
        ("2","female"),
        ("3","other"),
        ("4","unknown")
    )
    user = models.ForeignKey(Customer,on_delete= models.CASCADE)
    relationship = models.CharField(max_length=225, choices = RELATIONSHIP_CODE,null=True, blank=True)
    name = models.ForeignKey(HumanName,on_delete=models.CASCADE)
    telecom = models.ForeignKey(ContactPoint,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    gender = models.CharField(max_length=225, choices = GENDER_CODE,null=True, blank=True)
    #TODO: organization(Reference(Organization))
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    

class Communication(models.Model):
    """
    A language which may be used to communicate with the patient about his or her health.
    """
    LANGUAGE_CODE = (
        ("ar","Arabic"),	
        ("bn","Bengali"),	
        ("cs","Czech"),	
        ("da","Danish"),	
        ("de",	"German"),	
        ("de-AT",	"German (Austria)"),	
        ("de-CH",	"German (Switzerland)"),	
        ("de-DE",	"German (Germany)"),	
        ("el",	"Greek"),	
        ("en",	"English"),	
        ("en-AU",	"English (Australia)"),	
        ("en-CA",	"English (Canada)"),	
        ("en-GB",	"English (Great Britain)"),	
        ("en-IN",	"English (India)"),	
        ("en-NZ",	"English (New Zeland)"),	
        ("en-SG",	"English (Singapore)"),	
        ("en-US",	"English (United States)"),	
        ("es",	"Spanish"),	
        ("es-AR",	"Spanish (Argentina)"),	
        ("es-ES",	"Spanish (Spain)"),
        ("es-UY",	"Spanish (Uruguay)"),	
        ("fi",	"Finnish"),	
        ("fr",	"French"),	
        ("fr-BE",	"French (Belgium)"),	
        ("fr-CH",	"French (Switzerland)"),	
        ("fr-FR",	"French (France)"),	
        ("fy",	"Frysian"),	
        ("fy-NL",	"Frysian (Netherlands)"),	
        ("hi",	"Hindi"),	
        ("hr",	"Croatian"),	
        ("it",	"Italian"	),
        ("it-CH",	"Italian (Switzerland)"),	
        ("it-IT",	"Italian (Italy)"	),
        ("ja",	"Japanese"),
        ("ko",	"Korean"),
        ("ne","Nepali"),	
        ("nl",	"Dutch"), 	
        ("nl-BE",	"Dutch (Belgium)"),	
        ("nl-NL",	"Dutch (Netherlands)"),	
        ("no",	"Norwegian"),	
        ("no-NO",	"Norwegian (Norway)"),	
        ("pa",	"Punjabi"),	
        ("pl",	"Polish"),	
        ("pt",	"Portuguese"),	
        ("pt-BR",	"Portuguese (Brazil)"),	
        ("ru",	"Russian"),	
        ("ru-RU",	"Russian (Russia)"),	
        ("sr",	"Serbian"),	
        ("sr-RS",	"Serbian (Serbia)"),	
        ("sv",	"Swedish"),	
        ("sv-SE",	"Swedish (Sweden)"),	
        ("te",	"Telegu"),	
        ("zh",	"Chinese"),	
        ("zh-CN",	"Chinese (China)"),	
        ("zh-HK",	"Chinese (Hong Kong)"),	
        ("zh-SG",	"Chinese (Singapore)"),	
        ("zh-TW",	"Chinese (Taiwan)"),
    )
    
    user = models.ForeignKey(Customer,on_delete= models.CASCADE)
    language = models.CharField(max_length=225, choices=LANGUAGE_CODE, default="en-US",null=True, blank=True)
    preferred = models.BooleanField()

class Link(models.Model):
    """
    other-->(Reference(Patient/RelatedPerson))
    """
    TYPE_CODE = (
                 ("1","replaced-by"),
                 ("2","replaces"),
                 ("3","refer"),
                 ("4","seealso")
                 )
    #TODO : -->
    # other_patient = models.ForeignKey(Patient, models.CASCADE = on_delete)
    # other_relatedperson = models.ForeignKey(RelatedPerson, models.CASCADE = on_delete)
    
    user = models.ForeignKey(Customer,on_delete= models.CASCADE,null=True, blank=True)
    link_type = models.CharField(max_length=225, choices=TYPE_CODE,null=True, blank=True)

    def save(self, args, **kwargs):
        self.text = self.given +" "+self.family
        super(HumanName, self).save(*args, **kwargs)