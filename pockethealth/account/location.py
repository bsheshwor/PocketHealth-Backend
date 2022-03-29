from django.db import models
from django.conf import settings

class Status(models.Model):
    STATUS_CODE = (('active','Active'),
                   ('suspended','Suspended'),
                   ('inactive','Inactive'),)
    text = models.CharField(max_length=255, choices = STATUS_CODE)

class OperationalStatus(models.Model):
    OPERATIONAL_STATUS_CODE = (('C','Closed'),
                               ('H','HouseKeeping'),
                               ('I','Isolated'),
                               ('K','Contaminated'),
                               ('O','Occupied'),
                               ('U','Unoccupied'),)
    text = models.CharField(max_length=255, choices = OPERATIONAL_STATUS_CODE)

class Mode(models.Model):
    MODE_CODE = (('instance','Instance'),
                 ('kind','Kind'),
                 )

    text = models.CharField(max_length=255, choices = MODE_CODE)

class Type(models.Model):
    TYPE_CODE = (('','Diagnostics or therapeutics unit'),
                 ('','Cardiovascular diagnostics or therapeutics unit'),
                 ('','Cardiac catheterization lab'),
                 ('','Echocardiography lab'),
                 ('','Gastroenterology diagnostics or therapeutics lab'),
                 ('','Endoscopy lab'),
                 ('','Radiology diagnostics or therapeutics unit'),
                 ('','Radiation oncology unit'),
                 ('','Neuroradiology unit'),
                 ('','Hospital'),
                 ('','Chronic Care Facility'),
                 ('','Hospitals; General Acute Care Hospital'),
                 ('','Military Hospital'),
                 ('','Psychatric Care Facility'),
                 ('','Rehabilitation hospital'),
                 ('','addiction treatment center'),
                 ('','intellectual impairment center'),
                 ('','parents with adjustment difficulties center'),
                 ('','physical impairment center'),
                 ('','physical impairment - hearing center'),
                 ('','physical impairment - motor skills center'),
                 ('','physical impairment - visual skills center'),
                 ('','youths with adjustment difficulties center'),
                 ('','Hospital unit'),
                 ('','Bone marrow transplant unit'),
                 ('','Coronary care unit'),
                 ('','Chest unit'),
                 ('','Epilepsy unit'),
                 )
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

class Position(models.Model):
    #WANT THIS TO BE STORED AUTOMATICALLY
    #TODO: -->
    # longitude = decimal
    # latitude = decimal
    # altitude = decimal
    pass

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

class Location(models.Model):
    pass
    #identifier
    status = code
    operationalStatus = Coding
    name = models.CharField(max_length=15,null=True, blank=True) 
    alias = models.CharField(max_length=15,null=True, blank=True) 
    description = models.CharField(max_length=15,null=True, blank=True) 
    mode = code
    types = CodeableCOncept
    telecom = ContactPoint
    address = Address
    physicalType = CodeableCOncept
    position 
        longitude = decimal
        latitude = decimal
        altitude = decimal
    #managinOrganization= Reference(Organization)
    #partOf = Refernce(Location)
    hourseOfOperation 
       
    availabilityExceptions = models.CharField(max_length=15,null=True, blank=True) 