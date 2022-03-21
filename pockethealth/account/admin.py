from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User, Patient, Doctor
from account.types import Period,ContactPoint,Deceased,Address,HumanName,MaritalStatus,Contact,Communication,Link


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Period)
admin.site.register(ContactPoint)
admin.site.register(Deceased)
admin.site.register(Address)
admin.site.register(HumanName)
admin.site.register(MaritalStatus)
admin.site.register(Contact)
admin.site.register(Communication)
admin.site.register(Link)


