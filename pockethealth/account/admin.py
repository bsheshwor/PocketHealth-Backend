from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User, Patient, Practitioner
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Link,Telecom,RelatedPerson
from account.organization import Organization, OrganizationContact
from account.healthcareService import HealthcareService, HealthcareCategory, Type, Speciality, ServiceProvisionCode, Program,ReferralMethod, availableTime, notAvailableTime
from account.careteam import CareTeam, StatusCode, ParticipantRole, Participant, ReasonCode, Annotation, Author
from account.location import  Location, Status, OperationalStatus, Mode, Types, PhysicalLocationType, Position, HoursOfOperation


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Practitioner)
admin.site.register(Period)
admin.site.register(ContactPoint)
admin.site.register(Deceased)
admin.site.register(Address)
admin.site.register(HumanName)
admin.site.register(MaritalStatus)
admin.site.register(Contact)
admin.site.register(Communication)
admin.site.register(Telecom)
admin.site.register(Link)
admin.site.register(RelatedPerson)


admin.site.register(Organization)
admin.site.register(OrganizationContact)

admin.site.register(HealthcareService)
admin.site.register(HealthcareCategory)
admin.site.register(Type)
admin.site.register(Speciality)
admin.site.register(ServiceProvisionCode)
admin.site.register(Program)
admin.site.register(ReferralMethod)
admin.site.register(availableTime)
admin.site.register(notAvailableTime)

admin.site.register(CareTeam)
admin.site.register(StatusCode)
admin.site.register(ParticipantRole)
admin.site.register(Participant)
admin.site.register(ReasonCode)
admin.site.register(Annotation)
admin.site.register(Author)

admin.site.register(Location)
admin.site.register(Status)
admin.site.register(OperationalStatus)
admin.site.register(Mode)
admin.site.register(Types)
# admin.site.register(PhysicalLocationType)
admin.site.register(Position)
admin.site.register(HoursOfOperation)




