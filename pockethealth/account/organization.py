from django.db import models
from django.conf import settings
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Telecom,Link

class OrganizationContact(models.Model):
    PURPOSE_TYPE = (('BILL','Billing'),
                    ('ADMIN','Administrative'),
                    ('HR','Human Resource'),
                    ('PAYOR','Payor'),
                    ('PATINF','Patient'),
                    ('PRESS','Press'),)
    purpose =  models.CharField(max_length = 255, choices = PURPOSE_TYPE)
    organization = models.ForeignKey(Organization,related_name='contact',on_delete=models.CASCADE)

    # name = HumanName
    # telecom = ContactPoint
    # address = Address

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

    active = models.BooleanField()
    types = models.CharField(max_length= 255, choices= ORGANIZATION_TYPE)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    # telecom = models.CHar(contactpoint)
    #Address(Address)
    #partOf(Reference(Organization))
    # contact = OrganizationContact