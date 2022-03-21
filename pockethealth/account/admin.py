from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User, Patient, Practitioner
from account import patientModels


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Practitioner)
admin.site.register(patientModels.Period)
admin.site.register(patientModels.ContactPoint)
admin.site.register(patientModels.Deceased)
admin.site.register(patientModels.Address)
admin.site.register(patientModels.HumanName)
admin.site.register(patientModels.MaritalStatus)
admin.site.register(patientModels.Contact)
admin.site.register(patientModels.Communication)
admin.site.register(patientModels.Link)


