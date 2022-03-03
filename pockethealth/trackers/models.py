from turtle import window_height
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class BMIData(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    weight_in_kg = models.FloatField()
    height_in_cm = models.FloatField()
    bmi_result = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.bmi_result = self.weight_in_kg / ((self.height_in_cm * self.height_in_cm) / 10000)
        self.username = self.user.first_name
        super(BMIData, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.first_name + ' ' + str(self.created_at).split()[0]
    
    class Meta:
        verbose_name = "BMI"