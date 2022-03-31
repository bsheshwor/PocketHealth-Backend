from django.db import models
from django.conf import settings
from account.healthcareService import HealthcareService


class Location(models.Model):
    #identifier
    # status = code
    # operationalStatus = Coding
    name = models.CharField(max_length=15,null=True, blank=True) 
    alias = models.CharField(max_length=15,null=True, blank=True) 
    description = models.CharField(max_length=15,null=True, blank=True) 

    # mode = code
    # types = CodeableConcept
    # telecom = ContactPoint
    # address = Address
    # physicalType = CodeableCOncept
    # position 
    #managinOrganization= Reference(Organization)
    #partOf = Refernce(Location)
    # hourseOfOperation 
    availabilityExceptions = models.CharField(max_length=15,null=True, blank=True) 
    healthcareservice = models.ForeignKey(HealthcareService,related_name='location',on_delete=models.CASCADE)

class Status(models.Model):
    STATUS_CODE = (('active','Active'),
                   ('suspended','Suspended'),
                   ('inactive','Inactive'),)
    text = models.CharField(max_length=255, choices = STATUS_CODE)
    location = models.ForeignKey(Location,related_name='status',on_delete=models.CASCADE)

class OperationalStatus(models.Model):
    OPERATIONAL_STATUS_CODE = (('C','Closed'),
                               ('H','HouseKeeping'),
                               ('I','Isolated'),
                               ('K','Contaminated'),
                               ('O','Occupied'),
                               ('U','Unoccupied'),)
    text = models.CharField(max_length=255, choices = OPERATIONAL_STATUS_CODE)
    location = models.ForeignKey(Location,related_name='operationalStatus',on_delete=models.CASCADE)


class Mode(models.Model):
    MODE_CODE = (('instance','Instance'),
                 ('kind','Kind'),
                 )
    text = models.CharField(max_length=255, choices = MODE_CODE)
    location = models.ForeignKey(Location,related_name='mode',on_delete=models.CASCADE)

class Types(models.Model):
    TYPE_CODE = (('DX','Diagnostics or therapeutics unit'),
                 ('CVDX','Cardiovascular diagnostics or therapeutics unit'),
                 ('CATH','Cardiac catheterization lab'),
                 ('ECHO','Echocardiography lab'),
                 ('GIDX','Gastroenterology diagnostics or therapeutics lab'),
                 ('ENDOS','Endoscopy lab'),
                 ('RADDX','Radiology diagnostics or therapeutics unit'),
                 ('RADO','Radiation oncology unit'),
                 ('RNEU','Neuroradiology unit'),
                 ('HOSP','Hospital'),
                 ('CHR','Chronic Care Facility'),
                 ('GACH','Hospitals; General Acute Care Hospital'),
                 ('MHSP','Military Hospital'),
                 ('PSYCHF','Psychatric Care Facility'),
                 ('RH','Rehabilitation hospital'),
                 ('RHAT','addiction treatment center'),
                 ('RHII','intellectual impairment center'),
                 ('RHMAD','parents with adjustment difficulties center'),
                 ('RHPI','physical impairment center'),
                 ('RHPIH','physical impairment - hearing center'),
                 ('RHPIMS','physical impairment - motor skills center'),
                 ('RHPIVS','physical impairment - visual skills center'),
                 ('RHYAD','youths with adjustment difficulties center'),
                 ('HU','Hospital unit'),
                 ('BMTU','Bone marrow transplant unit'),
                 ('CCU','Coronary care unit'),
                 ('CHEST','Chest unit'),
                 ('EPIL','Epilepsy unit'),
                 )
    text = models.CharField(max_length=255, choices = TYPE_CODE)
    location = models.ForeignKey(Location,related_name='types',on_delete=models.CASCADE)

class PhysicalLocationType():
    PHYSICAL_CODE = (('si','Site'),
                     ('bu','Building'),
                     ('wi','Wing'),
                     ('wa','Ward'),
                     ('lvl','Level'),
                     ('co','Corridor'),
                     ('ro','Room'),
                     ('bd','Bed'),
                     ('ve','Vehicle'),
                     ('ho','House'),
                     ('ca','Cabinet'),
                     ('rd','Road'),
                     ('area','Area'),
                     ('jdn','Jurisdiction'),)
    text = models.CharField(max_length=255, choices = PHYSICAL_CODE)
    location = models.ForeignKey(Location,related_name='physicalType',on_delete=models.CASCADE)

class Position(models.Model):
    #WANT THIS TO BE STORED AUTOMATICALLY
    #TODO: --> make the longitude, latitude and altitude data storing process automatic
    longitude = models.DecimalField(max_digits = 255,
                                    decimal_places = 5)
    latitude = models.DecimalField(max_digits = 255,
                                    decimal_places = 5)
    altitude = models.DecimalField(max_digits = 255,
                                    decimal_places = 5)
    location = models.ForeignKey(Location,related_name='position',on_delete=models.CASCADE)

class HoursOfOperation(models.Model):
    DAYS_CODE = (('mon','Monday'),
                 ('tue','Tuesday'),
                 ('wed','Wednesday'),
                 ('thu','Thursday'),
                 ('fri','Friday'),
                 ('sat','Saturday'),
                 ('sun','Sunday'),)
    daysOfWeek = models.CharField(max_length=255, choices = DAYS_CODE)
    allDay = models.BooleanField()
    openingTime = models.TimeField(auto_now=False, auto_now_add=False)
    closingTime = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.ForeignKey(Location,related_name='hoursOfOperation',on_delete=models.CASCADE)
