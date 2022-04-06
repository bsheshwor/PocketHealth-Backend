from django.db import models
from django.conf import settings
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link


class HealthcareService(models.Model):
    #indentifier
    active = models.BooleanField(null=True, blank=True)
    # providedBy = Reference(Organization)
    # category = cODEABLEconcept
    # types =cODEABLEconcept 
    # speciality = cODEABLEconcept
    # location = Refernce(Location)
    name = models.CharField(max_length = 255,null=True, blank=True)
    comment = models.CharField(max_length = 255,null=True, blank=True)
    # "extraDetails": "Several assessments are required for these specialist services, and the waiting times can be greater than 3 months at times. Existing patients are prioritized when requesting appointments on the schedule."
    #TODO: --> extraDetails = Markdown
    #TODO: photo = Attachment
    # Telecom = ContactPoint
    #TODO coverageArea = ReferenceLocation
    # serviceProvisionCode = COdeableConcept
    #confused about elligibility
    # TODO: eligibility 
    #     code = COdeableCOncept
    #     comment = MarkDown
    
    # program= COdeableCOncept 

    #CONFUSED ABOUT CHARACTERISTIC
    # characteristic= COdeableCOncept

    # Communication= COdeableCOncept

    # referralMethod= COdeableCOncept
    appointmentRequired = models.BooleanField(null=True, blank=True)
    # availableTIme
    #     daysOfWeek = code
    #     allDay = boolean
    #     availableStartTIme = time
    #     availabelEndTIme = time
    # notAvailable
    #     description = string
    #     during = period
    availabilityExceptions = models.CharField(max_length = 255,null=True, blank=True)

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
    text = models.CharField(max_length = 255, choices = CATEGORY_TYPE,null=True, blank=True)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='category',on_delete=models.CASCADE,null=True, blank=True)

class Type(models.Model):
    TYPE_CHOICES = (('5','Case Management for Older Persons	'),	
				('30','Reiki'),
				('60','Nutrition'),
				('64','Pharmacy'),
				('58','Maternal & Child Health	'),
				('51','Blood Donation	'),
				('88','General Dental'),
				('117','Emergency Medical	'),
				('102','Disability Supported Accommodation'),
				('136','Mental Health Case Management'),
				('151','Yoga'),
				('159','Pathology - General'),
				('165','Cardiology'),
				('177','Neurology'),
				('216','Neurosurgery'),
				('226','Ambulance'),
				('227','Blood Transport'),
				('254','Asthma'),
				('251','Arthritis'),
				('268','Bone'),
				('270','Brain'),
				('284','Child Care'),
				('316','Depression'),
				('318','Diabetes'),
				('396','Oral Hygiene'),
				('380','Lung'),
				('410','Pregnancy'))

    text = models.CharField(max_length = 255, choices = TYPE_CHOICES,null=True, blank=True)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='types',on_delete=models.CASCADE,null=True, blank=True)


class Speciality(models.Model):
    # speciality
    SPECILAITY_CHOICES =(('394579002','Cardiology'),
                ('408462000','Burns Care'),
                ('394577000','Anesthetics'),
                ('421661004','Blood banking and transfusion medicine'),
                ('408478003','Critical care medicine'),
                ('394812008','Dental medicine specialties'),
                ('394582007','Dermatology'),
                ('408475000','Diabetic Medicine'),
                ('394802001','General medicine'),
                ('394586005','Gynecology'),
                ('394591006','Neurology'),
                ('394914008','Radiology'),
                ('394602003','Rehabilitation'),
                ('394810000','Rheumatology'),
                ('394609007','Surgery-general'),
                ('394612005','Urology'))

    text = models.CharField(max_length = 255, choices = SPECILAITY_CHOICES,null=True, blank=True)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='speciality',on_delete=models.CASCADE,null=True, blank=True)

class ServiceProvisionCode(models.Model):
    SERVICE_PROVISION_CODE = (('free','Free'),
                              ('disc','Discounts Available'),
                              ('cost','Fees apply'),)
    text = models.CharField(max_length = 255, choices = SERVICE_PROVISION_CODE,null=True, blank=True)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='serviceProvisionCode',on_delete=models.CASCADE,null=True, blank=True)

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
    text = models.CharField(max_length = 255, choices = PROGRAM_CODE,null=True, blank=True)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='program',on_delete=models.CASCADE,null=True, blank=True)

#TODO: > characteristics and communication left-->

class ReferralMethod(models.Model):
    REFERRAL_CODE = (('fax','Fax'),
                     ('phone','Phone'),
                     ('elec','Secure Messaging'),
                     ('semail','Secure Email'),
                     ('mail','Mail'),
                    ) 
    text = models.CharField(max_length = 255, choices = REFERRAL_CODE,null=True, blank=True)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='referralMethod',on_delete=models.CASCADE,null=True, blank=True)

class availableTime(models.Model):
    DAYS_CODE = (('mon','Monday'),
                 ('tue','Tuesday'),
                 ('wed','Wednesday'),
                 ('thu','Thursday'),
                 ('fri','Friday'),
                 ('sat','Saturday'),
                 ('sun','Sunday'),)
    daysOfWeek = models.CharField(max_length = 255, choices = DAYS_CODE,null=True, blank=True)
    allDay = models.BooleanField(null=True, blank=True)
    availableStartTime =  models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    availabelEndTime =  models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='availableTime',on_delete=models.CASCADE,null=True, blank=True)

class notAvailableTime(models.Model):
    description= models.CharField(max_length = 255,null=True, blank=True)
    # during = Period
    healthcareservice = models.ForeignKey(HealthcareService,related_name='notAvailable',on_delete=models.CASCADE,null=True, blank=True)

