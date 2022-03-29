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



    ROLES_TYPES = (('375005','Sibling'),
                    ('Adoptive Father','609005'),
                    ('9947008','Natural Father'),
                    ('9306000','Legal Parent'),
                    ('13646006','Natural Parent'),
                    ('14469008','Legal Child'),
                    ('19343003','Twin sister'),
                    ('15130002','Surrogate Parent'),
                    ('21464003','Adoptive Mother'),
                    ('34871008','Grand Father'),
                    ('34591001','Niece'),
                    ('33969000','Great-Grand Parent'),
                    ('40683002','Parent'),
                    ('55538000','Cousin'),
                    ('60614009','Natural Brother'),
                    ('65616008','Son'),
                    ('65656005','Natural Mother'),
                    ('65853000','Student'),
                    ('66089001','Daughter'),
                    ('66839005','Father'),
                    ('70578009','Grand Son'),
                    ('72705000','Mother'),
                    ('82101005','Natural Sibbling'),
                    ('83559000','Nephew'),
                    ('105456007','Live Donor'),
                    ('105458008','Candidate Donor'),
                    ('105459000','Accepted Doner'),
                    ('105461009','Orgran Donor'),
                    ('105471007','Blood Donor'),
                    ('113158001','Grandmother'),
                    ('116154003','Patient'),
                    ('127849001','Husband'),
                    ('127850001','Wife'),
                    ('133933007','NewBorn'),
                    ('133936004','Adult'))

    REASON_CODE = (('219006','Alcohol User'),
                    ('237009','Acute myringitis'),
                    ('368009','Heart valve disorder	'),
                    ('409002','Food allergy diet'),
                    ('165002','Accident-prone'),
                    ('199004','Decreased Lactation'),
                    ('437009','Abnormal Composition of urine'),
                    ('488007','Fibroid Myocarditis'),
                    ('652005','Ganfrenois tonsilitis'),
                    ('675003','Torsion of intestine'),
                    ('788006','Disease related Diet'),
                    ('8549000','Total Cataract'),
                    ('1108009','Female pattern alopecia'),
                    ('1208004','Gastroptosis'),
                    ('1427008','Intraspinal abscess'),
                    ('1939005','Abnormal vascular flow	'),
                    ('2043009','Alcoholic gastritis'),
                    ('2388001','Normal variation in translucency'),  
                    ('2999009','Injury of ear region	'),
                    ('3002002','Thyroid Hemorrhage'),
                    ('3095005','Induced malaria'),
                    ('3640000','Late effect of traumatic amputation'),
                    ('3712000','Degenerated eye'),
                    ('3716002','Thyroid goiter'),
                    ('4448006','Allergic headache	'),    
                    ('4473006','Migraine with aura')
                    ('9999999999','Others')
                    )

    