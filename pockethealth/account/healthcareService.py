from django.db import models
from django.conf import settings
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link

class HealthcareCategory(models.Model):
    CATEGORY_TYPE = (("1","Adoption"),
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
    text = models.CharField(max_length = 255, choices = CATEGORY_TYPE)

class ServiceProvisionCode(models.Model):
    SERVICE_PROVISION_CODE = (('free','Free'),
                              ('disc','Discounts Available'),
                              ('cost','Fees apply'),)
    text = models.CharField(max_length = 255, choices = SERVICE_PROVISION_CODE)

class Program(models.Model):

    PROGRAM_CODE = (('1','Acquired Brain Injury (ABI) Program '),
                    ('2','ABI Slow To Recover (ABI STR) Program'),
                    ('3','Access Programs'),
                    ('4','Adult and Further Education (ACFE) Program'),
                    ('5','Adult Day Activity and Support Services (ADASS) Program'),
                    ('6','Adult Day Care Program'),
                    ('7','ATSS (Adult Training Support Service)'),
                    ('8','Community Aged Care Packages (CACP)'),
                    ('9','Care Coordination & Supplementary Services (CCSS)'),
                    ('10','Cognitive Dementia Memory Service (CDAMS)'),
                    ('11','ChildFIRST'),
                    ('12','Childrens Contact Services'),
                    ('13','Community Visitors Scheme'),
                    ('14','CPP (Community Partners Program)'),
                    ('15','Closing the Gap (CTG)'),
                    ('16','Coordinated Veterans Care (CVC) Program'),
                    ('17','Day Program'),
                    ('18','Drop In Program'),
                    ('19','Early Years Program'),
                    ('20','Employee Assistance Program'),
                    ('21','Home And Community Care (HACC)'),
                    ('22','Hospital Admission Risk Program (HARP)'),
                    ('23','Hospital in the Home (HITH) Program'),
                    ('24','ICTP (Intensive Community Treatment Program)'),
                    ('25','IFSS (Intensive Family Support Program)'),
                    ('26','JPET (Job Placement, Education and Training)'),
                    ('27','Koori Juvenile Justice Program'),
                    ('28','Language Literacy and Numeracy Program'),
                    ('29','Life Skills Program'),
                    ('30','LMP (Lifestyle Modification Program)'),
                    ('31','MedsCheck Program'),
                    ('32','Methadone/Buprenorphine Program'),
                    ('33','National Disabilities Insurance Scheme (NDIS)'),
                    ('34','National Diabetes Services Scheme (NDSS)'),
                    ('35','Needle/Syringe Program'),
                    ('36','nPEP Program'),
                    ('37','Personal Support Program'),
                    ('38','Partners in Recovery (PIR) Program'),
                    ('39','Pre-employment Program'),
                    ('40','Reconnect Program'),
                    ('41','Sexual Abuse Counselling and Prevention Program (SACPP)'),
                    ('42','Social Support Programs'),
                    ('43','Supported Residential Service (SRS)'),
                    ('44','Tasmanian Aboriginal Centre (TAC)'),
                    ('45','Victims Assistance Program'),
                    )
    text = models.CharField(max_length = 255, choices = PROGRAM_CODE)

class ReferralMethod(models.Model):
    REFERRAL_CODE = (('fAX','Fax'),
                     ('phone','Phone'),
                     ('elec','Secure Messaging'),
                     ('semail','Secure Email'),
                     ('mail','Mail'),
                    ) 
    text = models.CharField(max_length = 255, choices = REFERRAL_CODE)

class availableTime(models.Model):
    DAYS_CODE = (('mon','Monday'),
                 ('tue','Tuesday'),
                 ('wed','Wednesday'),
                 ('thu','Thursday'),
                 ('fri','Friday'),
                 ('sat','Saturday'),
                 ('sun','Sunday'),)
    daysOfWeek = models.CharField(max_length = 255, choices = DAYS_CODE)
    allDay = models.BooleanField()
    availableStartTIme =  models.TimeField(auto_now=False, auto_now_add=False)
    availabelEndTIme =  models.TimeField(auto_now=False, auto_now_add=False)

class notAvailabelTime(models.Model):
    description= models.CharField(max_length = 255)
    during = Period

class HealthcareService(models.Model):
    #indentifier
    active = models.BooleanField()
    # providedBy = Reference(Organization)
    Category = cODEABLEconcept
    types =cODEABLEconcept 
    speciality = cODEABLEconcept
    location = Refernce(Location)
    name = models.CharField(max_length = 255)
    comment = models.CharField(max_length = 255)
    # "extraDetails": "Several assessments are required for these specialist services, and the waiting times can be greater than 3 months at times. Existing patients are prioritized when requesting appointments on the schedule."
    extraDetails = Markdown
    photo = Attachment
    Telecom = ContactPoint
    coverageArea = ReferenceLocation
    serviceProvisionCode = COdeableConcept
    #confused about elligibility
    eligibility 
        code = COdeableCOncept
        comment = MarkDown
    
    program= COdeableCOncept 

    #CONFUSED ABOUT CHARACTERISTIC
    characteristic= COdeableCOncept

    Communication= COdeableCOncept

    referralMethod= COdeableCOncept
    appointmentRequired = models.BooleanField()
    availableTIme
        daysOfWeek = code
        allDay = boolean
        availableStartTIme = time
        availabelEndTIme = time
    notAvailable
        description = string
        during = period
    availabilityExceptions = models.CharField(max_length = 255)