from django.db import models
from django.conf import settings


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
    
    # user = models.ForeignKey(Patient, related_name="marital_status",on_delete= models.CASCADE)
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
    # user = models.ForeignKey(Patient, related_name="contact",on_delete= models.CASCADE)
    relationship = models.CharField(max_length=225, choices = RELATIONSHIP_CODE,null=True, blank=True)
    # name = models.ForeignKey(HumanName,on_delete=models.CASCADE)
    # telecom = models.ForeignKey(ContactPoint,on_delete=models.CASCADE)
    # address = models.ForeignKey(Address,on_delete=models.CASCADE)
    gender = models.CharField(max_length=225, choices = GENDER_CODE,null=True, blank=True)
    #TODO: organization(Reference(Organization))
    # period = models.ForeignKey(Period, on_delete=models.CASCADE)




class Deceased(models.Model):
    """
    Indicates if the individual is deceased or not
    """

    # user = models.ForeignKey(Patient, related_name="deceased",on_delete= models.CASCADE)
    deceasedBoolean = models.BooleanField()
    # deceasedDateTime = models.BooleanField()



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
    # user = models.ForeignKey(Patient, related_name="human_name",on_delete= models.CASCADE)
    use = models.CharField(max_length=225, choices=USE_CODE, default="2",null=True, blank=True)
    text = models.CharField(max_length=225,null=True, blank=True)
    family = models.CharField(max_length=225,null=True, blank=True)
    given = models.CharField(max_length=225,null=True, blank=True)
    prefix = models.CharField(max_length=10,null=True, blank=True)
    suffix = models.CharField(max_length= 225,null=True, blank=True)
    contact = models.ForeignKey(Contact,related_name='name',on_delete=models.CASCADE)

    def save(self, args, **kwargs):
        self.text = self.given +" "+self.family
        super(HumanName, self).save(*args, **kwargs)

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

    # user = models.ForeignKey(Patient, related_name="contact_point",on_delete= models.CASCADE)

    system = models.CharField(max_length=20, choices= SYSTEM_CHOICES,null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    use = models.CharField(max_length=255, choices = USE_CODE, null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)

    # period = models.OneToOneField(Period,on_delete=models.CASCADE,null=True, blank=True)

class Telecom(ContactPoint):
    contact = models.ForeignKey(Contact,related_name='telecom',on_delete=models.CASCADE)


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
    # user = models.ForeignKey(Patient, related_name="address",on_delete= models.CASCADE)
    use = models.CharField(max_length=225, choices = ADDRESS_USE_CHOICES,null=True, blank=True)
    address_type = models.CharField(max_length=40, choices= ADDRESS_TYPE_CHOICES,null=True, blank=True)
    text = models.CharField(max_length=500,null=True, blank=True)
    line = models.CharField(max_length=225,null=True, blank=True)
    city = models.CharField(max_length=225,null=True, blank=True)
    district = models.CharField(max_length=225,null=True, blank=True)
    state = models.CharField(max_length=225,null=True, blank=True)
    postalCode = models.CharField(max_length=225,null=True, blank=True)
    country = models.CharField(max_length=225,null=True, blank=True)
    contact = models.ForeignKey(Contact,related_name='address',on_delete=models.CASCADE)


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
    
    # user = models.ForeignKey(Patient, related_name="communication",on_delete= models.CASCADE)
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
    
    # user = models.ForeignKey(Patient, related_name="link", on_delete= models.CASCADE,null=True, blank=True)
    link_type = models.CharField(max_length=225, choices=TYPE_CODE,null=True, blank=True)


#TODO : -->
#general practitioner
#managingOrganization
#providedBy-->Reference(Organization)

class Category(models.Model):

    SERVICE_CODE = (("1","Adoption"),
                    ("2","Aged Care"),
                    ("34","Allied Health"),
                    ("3","Alternative/Complementary Therapies"),
                    ("4","Child Care /Kindergarten"),
                    ("5","Child Development"),
                    ("6","Child Protection & Family Services"),
                    ("7","	Community Health Care"),
                    ("8","Counselling"),
                    ("36","Crisis Line (GPAH use only)"),
                    ("9","Death Services"),
                    ("10","Dental"),
                    ("11","Disability Support"),
                    ("12","Drug/Alcohol"),
                    ("13","Education & Learning"),
                    ("14","Emergency Department"),
                    ("15","Employment"),
                    ("16","Financial & Material Aid"),
                    ("17","General Practice"),
                    ("35","Hospital"),
                    ("18","Housing/Homelessness"),
                    ("19","Interpreting"),
                    ("20","Justice"),
                    ("21","Legal"),
                    ("22","Mental Health"),
                    ("38","NDIA"),
                    ("23","Physical Activity & Recreation"),
                    ("24","Regulation"),
                    ("25","Respite/Carer Support"),
                    ("26","Specialist Clinical Pathology"),
                    ("27","Specialist Medical"),
                    ("28","Specialist Obstetrics & Gynecology"),
                    ("29","Specialist Paediatric"),
                    ("30","Specialist Radiology/Imaging"),
                    ("31","Specialist Surgical"),
                    ("32","Support Group/s"),
                    ("37","Test Message (HSD admin)"),
                    ("33","Transport"),
                   )
    text = models.CharField(max_length=225, null=True, blank = True)

class Period(models.Model):
    # user = models.ForeignKey(Patient, related_name="period",on_delete= models.CASCADE)
    start = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    end = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    contactpoint = models.OneToOneField(ContactPoint,related_name='period',on_delete=models.CASCADE,null=True, blank=True)
    address = models.ForeignKey(Address,related_name='period', on_delete= models.CASCADE,null=True, blank=True)
    humanname = models.ForeignKey(HumanName,related_name='period',on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact,related_name='period', on_delete=models.CASCADE)

#todo:typeclass (what to do?  more than 600 types)

#speciality: ??
