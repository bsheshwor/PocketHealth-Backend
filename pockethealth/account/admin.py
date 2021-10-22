from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User, Customer, Doctor


admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Doctor)
