from django.db import models
from django.conf import settings
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link
from account.careteam import CareTeam, Participant 
from account.healthcareService import HealthcareService
from account.location import Location

class Organization(models.Model):
    #indentifiers

    ORGANIZATION_TYPE = (('prob','Healthcare Provider'),
                         ('dept','Hospital Department'),
                         ('team','Organizational Team'),
                         ('govt','Government'),
                         ('ins','Insurance Company'),
                         ('pay','Payer'),
                         ('edu','Educational Institute'),
                         ('reli','Religious Institution'),
                         ('crs','Clinical Research Sponsor'),
                         ('cg','Community Group'),
                         ('bus','Non-Healthcare Business or Corporation'),
                         ('other','Other'),)

    active = models.BooleanField(null=True, blank=True)
    types = models.CharField(max_length= 255, choices= ORGANIZATION_TYPE,null=True, blank=True)
    name = models.CharField(max_length=255,null=True, blank=True)
    alias = models.CharField(max_length=255,null=True, blank=True)
    careteam = models.ForeignKey(CareTeam,related_name='managingOrganization',on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant,related_name='onBehalfOf',on_delete=models.CASCADE)
    healthcareservice = models.ForeignKey(HealthcareService,related_name='providedBy',on_delete=models.CASCADE)
    location = models.ForeignKey(Location,related_name='managingOrganization',on_delete=models.CASCADE)

    # telecom = models.CHar(contactpoint)
    #Address(Address)
    #partOf(Reference(Organization))
    # contact = OrganizationContact

class OrganizationContact(models.Model):
    PURPOSE_TYPE = (('BILL','Billing'),
                    ('ADMIN','Administrative'),
                    ('HR','Human Resource'),
                    ('PAYOR','Payor'),
                    ('PATINF','Patient'),
                    ('PRESS','Press'),)
    purpose =  models.CharField(max_length = 255, choices = PURPOSE_TYPE,null=True, blank=True)
    organization = models.ForeignKey(Organization,related_name='contact',on_delete=models.CASCADE)

    # name = HumanName
    # telecom = ContactPoint
    # address = Address
