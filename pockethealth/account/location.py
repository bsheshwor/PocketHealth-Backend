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
    healthcareservice = models.ForeignKey(HealthcareService,related_name='location',on_delete=models.CASCADE,null=True, blank=True)

class Status(models.Model):
    STATUS_CODE = (('active','Active'),
                   ('suspended','Suspended'),
                   ('inactive','Inactive'),)
    text = models.CharField(max_length=255, choices = STATUS_CODE,null=True, blank=True)
    location = models.ForeignKey(Location,related_name='status',on_delete=models.CASCADE,null=True, blank=True)

class OperationalStatus(models.Model):
    OPERATIONAL_STATUS_CODE = (('C','Closed'),
                               ('H','HouseKeeping'),
                               ('I','Isolated'),
                               ('K','Contaminated'),
                               ('O','Occupied'),
                               ('U','Unoccupied'),)
    text = models.CharField(max_length=255, choices = OPERATIONAL_STATUS_CODE,null=True, blank=True)
    location = models.ForeignKey(Location,related_name='operationalStatus',on_delete=models.CASCADE,null=True, blank=True)


class Mode(models.Model):
    MODE_CODE = (('instance','Instance'),
                 ('kind','Kind'),
                 )
    text = models.CharField(max_length=255, choices = MODE_CODE,null=True, blank=True)
    location = models.ForeignKey(Location,related_name='mode',on_delete=models.CASCADE,null=True, blank=True)

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
    text = models.CharField(max_length=255, choices = TYPE_CODE,null=True, blank=True)
    location = models.ForeignKey(Location,related_name='types',on_delete=models.CASCADE,null=True, blank=True)

class PhysicalLocationType(models.Model):
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
    text = models.CharField(max_length=255, choices = PHYSICAL_CODE,null=True, blank=True)
    location = models.ForeignKey(Location,related_name='physicalType',on_delete=models.CASCADE,null=True, blank=True)

class Position(models.Model):
    #WANT THIS TO BE STORED AUTOMATICALLY
    #TODO: --> make the longitude, latitude and altitude data storing process automatic
    longitude = models.DecimalField(max_digits = 255,
                                    decimal_places = 5,null=True, blank=True)
    latitude = models.DecimalField(max_digits = 255,
                                    decimal_places = 5,null=True, blank=True)
    altitude = models.DecimalField(max_digits = 255,
                                    decimal_places = 5,null=True, blank=True)
    location = models.ForeignKey(Location,related_name='position',on_delete=models.CASCADE,null=True, blank=True)

class HoursOfOperation(models.Model):
    DAYS_CODE = (('mon','Monday'),
                 ('tue','Tuesday'),
                 ('wed','Wednesday'),
                 ('thu','Thursday'),
                 ('fri','Friday'),
                 ('sat','Saturday'),
                 ('sun','Sunday'),)
    daysOfWeek = models.CharField(max_length=255, choices = DAYS_CODE,null=True, blank=True)
    allDay = models.BooleanField(null=True, blank=True)
    openingTime = models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    closingTime = models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    location = models.ForeignKey(Location,related_name='hoursOfOperation',on_delete=models.CASCADE,null=True, blank=True)
