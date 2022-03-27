from django.db import models
from django.conf import settings

class Participant(models.Model):
     role = CodeableConcept
    # member = Reference(Practitioner | PractitionerRole | RelatedPerson | Patient | Organization | CareTeam)
    # onBehalfOf = Refernce(Organization)
    # period = Period 

class CareTeam(models.Model):
    #IDENTIFIER
    status = code
    category = CodeableConcept
    name = models.CharField(max_length=15,null=True, blank=True)  
    #subject = Reference(Patient | Group)
    #encounter = Reference(Encounter)
    #period = Period
    participant
        role = CodeableConcept
        # member = Reference(Practitioner | PractitionerRole | RelatedPerson | Patient | Organization | CareTeam)
        # onBehalfOf = Refernce(Organization)
        # period = Period
    reasonCode = CodeableConcept
    # reasonReference = Reference(COndition)
    # managingOrganization = Refernce(Organization)
    telecom = ContactPoint
    note = Annotation