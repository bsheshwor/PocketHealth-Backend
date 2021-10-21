from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import UserProfile, Customer, Doctor

# class MyUserAdmin(UserAdmin):
#     model = UserProfile
#     list_display = ['id', 'email','name', 'is_active', 'is_staff', 'is_customer', 'is_doctor' ]
#     ordering = ['id']


# class CustomerAdmin(admin.ModelAdmin):
#     model = Customer
#     list_display = ['id', 'email','name', 'is_active', 'is_staff', 'is_customer', 'is_doctor' ]
#     ordering = ['user__id']


# class DoctorAdmin(admin.ModelAdmin):
#     model = Doctor
#     list_display = ['id', 'email','name', 'is_active', 'is_staff', 'is_customer', 'is_doctor' ]
#     ordering = ['user__id']


# admin.site.register(UserProfile, MyUserAdmin)
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Doctor, DoctorAdmin)

admin.site.register(UserProfile)
