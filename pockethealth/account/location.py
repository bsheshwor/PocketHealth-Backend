from django.db import models
from django.conf import settings

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
    longitude = decimal
    latitude = decimal
    altitude = decimal

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