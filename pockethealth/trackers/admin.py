from django.contrib import admin

# Register your models here.
from trackers.models import BMIData, BloodSugarData, PressureData

@admin.register(BMIData)
class BMIAdmin(admin.ModelAdmin):
    search_fields = ("created_at", )
    list_display = ('username', 'bmi_result', 'created_at', 'updated_at')

@admin.register(PressureData)
class PressureAdmin(admin.ModelAdmin):
    search_fields = ("created_at", )
    list_display = ('username', 'value', 'created_at', 'updated_at')

@admin.register(BloodSugarData)
class BloodSugarAdmin(admin.ModelAdmin):
    search_fields = ("created_at", )
    list_display = ('username', 'value', 'created_at', 'updated_at')

# admin.site.register(BMIData)

# admin.site.register(File)

# @admin.register(Attachment)
# class AttachmentAdmin(admin.ModelAdmin):
#     exclude = ()