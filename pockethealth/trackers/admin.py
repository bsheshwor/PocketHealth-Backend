from django.contrib import admin

# Register your models here.
from trackers.models import BMIData

@admin.register(BMIData)
class BMIAdmin(admin.ModelAdmin):
    exclude = ('username', 'bmi_result')
    
    search_fields = ("created_at", )
    list_display = ('username', 'bmi_result', 'created_at', 'updated_at')
  
# admin.site.register(BMIData)
