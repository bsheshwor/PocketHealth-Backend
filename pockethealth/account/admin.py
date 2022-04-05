from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User, Patient, Practitioner, PatientRegisterModel,PractitionerRegisterModel
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Link,Telecom,RelatedPerson,Qualification, QualificationCodeableConcept
from account.organization import Organization, OrganizationContact
from account.healthcareService import HealthcareService, HealthcareCategory, Type, Speciality, ServiceProvisionCode, Program,ReferralMethod, availableTime, notAvailableTime
from account.careteam import CareTeam, StatusCode, ParticipantRole, Participant, ReasonCode, Annotation, Note,Author
from account.location import  Location, Status, OperationalStatus, Mode, Types, PhysicalLocationType, Position, HoursOfOperation

class PatientRegisterModelInline(admin.TabularInline):
    model = PatientRegisterModel

class PractitionerRegisterModelInline(admin.TabularInline):
    model = PractitionerRegisterModel


class PeriodInline(admin.TabularInline):
    model = Period

class HumanNameInline(admin.TabularInline):
    model = HumanName

class TelecomInline(admin.TabularInline):
    model = Telecom

class AddressInline(admin.TabularInline):
    model = Address

class DeceasedInline(admin.TabularInline):
    model = Deceased

class MaritalStatusInline(admin.TabularInline):
    model = MaritalStatus

class ContactPointInline(admin.TabularInline):
    model = ContactPoint

class ContactInline(admin.TabularInline):
    model = Contact

class CommunicationInline(admin.TabularInline):
    model = Communication

class LinkInline(admin.TabularInline):
    model = Link

class OrganizationContactInline(admin.TabularInline):
    model = OrganizationContact

class OrganizationInline(admin.TabularInline):
    model = Organization

class HealthcareCategoryInline(admin.TabularInline):
    model = HealthcareCategory

class TypeInline(admin.TabularInline):
    model = Type

class SpecialityInline(admin.TabularInline):
    model = Speciality

class ServiceProvisionCodeInline(admin.TabularInline):
    model = ServiceProvisionCode

class ProgramInline(admin.TabularInline):
    model = Program

class ReferralMethodInline(admin.TabularInline):
    model = ReferralMethod

class availableTimeInline(admin.TabularInline):
    model = availableTime

class notAvailableTimeInline(admin.TabularInline):
    model = notAvailableTime

class HealthcareServiceInline(admin.TabularInline):
    model = HealthcareService

class StatusCodeInline(admin.TabularInline):
    model = StatusCode

class ParticipantRoleInline(admin.TabularInline):
    model = ParticipantRole

class ParticipantInline(admin.TabularInline):
    model = Participant

class ReasonCodeInline(admin.TabularInline):
    model = ReasonCode

class AnnotationInline(admin.TabularInline):
    model = Annotation

class NoteInline(admin.TabularInline):
    model = Note

class AuthorInline(admin.TabularInline):
    model = Author

class CareTeamInline(admin.TabularInline):
    model = CareTeam

class StatusInline(admin.TabularInline):
    model = Status

class OperationalStatusInline(admin.TabularInline):
    model = OperationalStatus

class ModeInline(admin.TabularInline):
    model = Mode

class TypesInline(admin.TabularInline):
    model = Types

class PhysicalLocationTypeInline(admin.TabularInline):
    model = PhysicalLocationType

class PositionInline(admin.TabularInline):
    model = Position

class HoursOfOperationInline(admin.TabularInline):
    model = HoursOfOperation

class LocationInline(admin.TabularInline):
    model = Location

class QualificationInline(admin.TabularInline):
    model = Qualification

class QualificationCodeableConceptInline(admin.TabularInline):
    model = QualificationCodeableConcept

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Practitioner)
admin.site.register(Period)


@admin.register(ContactPoint)
class ContactPointAdmin(admin.ModelAdmin):
    inlines = [PeriodInline,]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    inlines = [PeriodInline,]

@admin.register(Telecom)
class TelecomAdmin(admin.ModelAdmin):
    inlines = [PeriodInline,]

@admin.register(HumanName)
class HumanNameAdmin(admin.ModelAdmin):
    inlines = [PeriodInline,]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [HumanNameInline,TelecomInline,AddressInline,PeriodInline]

@admin.register(OrganizationContact)
class OrganizationContactAdmin(admin.ModelAdmin):
    inlines = [TelecomInline,AddressInline]

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [TelecomInline,AddressInline, ContactInline]

# @admin.register(notAvailableTime)
# class notAvailableTimeAdmin(admin.ModelAdmin):
#     inlines = [during,]

@admin.register(HealthcareService)
class HealthcareServiceAdmin(admin.ModelAdmin):
    inlines = [HealthcareCategoryInline, TypeInline, SpecialityInline, TelecomInline, ServiceProvisionCodeInline,ProgramInline,CommunicationInline, ReferralMethodInline, availableTimeInline, notAvailableTimeInline]

@admin.register(CareTeam)
class CareTeamAdmin(admin.ModelAdmin):
    inlines = [StatusCodeInline, PeriodInline,ReasonCodeInline,OrganizationInline, TelecomInline,NoteInline]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    inlines = [AnnotationInline,]


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    inlines = [ParticipantRoleInline, OrganizationInline, PeriodInline]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [StatusInline, OperationalStatusInline, ModeInline, TypesInline, TelecomInline, AddressInline, PhysicalLocationTypeInline, PositionInline, OrganizationInline, HoursOfOperationInline]

@admin.register(PatientRegisterModel)
class PatientRegisterAdmin(admin.ModelAdmin):
    inlines = [HumanNameInline, TelecomInline, AddressInline, MaritalStatusInline, ContactInline, CommunicationInline, OrganizationInline, LinkInline]


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    inlines = [QualificationCodeableConceptInline,PeriodInline]


@admin.register(PractitionerRegisterModel)
class PractitionerRegisterAdmin(admin.ModelAdmin):
    inlines = [HumanNameInline, TelecomInline, AddressInline,QualificationInline,CommunicationInline]

admin.site.register(Deceased)
# admin.site.register(Address)
# admin.site.register(HumanName)
admin.site.register(MaritalStatus)
# admin.site.register(Contact)
admin.site.register(Communication)
# admin.site.register(Telecom)
admin.site.register(Link)
admin.site.register(RelatedPerson)
# admin.site.register(Qualification)
admin.site.register(QualificationCodeableConcept)


# admin.site.register(Organization)
# admin.site.register(OrganizationContact)

# admin.site.register(HealthcareService)
admin.site.register(HealthcareCategory)
admin.site.register(Type)
admin.site.register(Speciality)
admin.site.register(ServiceProvisionCode)
admin.site.register(Program)
admin.site.register(ReferralMethod)
admin.site.register(availableTime)
admin.site.register(notAvailableTime)

# admin.site.register(CareTeam)
admin.site.register(StatusCode)
admin.site.register(ParticipantRole)
# admin.site.register(Participant)
admin.site.register(ReasonCode)
admin.site.register(Annotation)
admin.site.register(Author)

# admin.site.register(Location)
admin.site.register(Status)
admin.site.register(OperationalStatus)
admin.site.register(Mode)
admin.site.register(Types)
# admin.site.register(PhysicalLocationType)
admin.site.register(Position)
admin.site.register(HoursOfOperation)




