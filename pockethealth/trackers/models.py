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

class PressureData(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.username = self.user.first_name
        super(PressureData, self).save(*args, **kwargs)
        
    def __str__(self): 
        return self.user.first_name + ' ' + str(self.created_at).split()[0]
    
    class Meta:
        verbose_name = "Pressure"

class BloodSugarData(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.username = self.user.first_name
        super(BloodSugarData, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.first_name + ' ' + str(self.created_at).split()[0]
    
    class Meta:
        verbose_name = "BloodSugar"











# from .validators import validate_file_size

# class File(models.Model):
#     name= models.CharField(max_length=500)
#     filepath= models.FileField(upload_to='files/', verbose_name="", validators=[validate_file_size])

#     def __str__(self):
#         return self.name + ": " + str(self.filepath)


# import os
# import hashlib
# from django.core.files.base import ContentFile
# import base64

# class Attachment(models.Model):
#     contentType = models.CharField(max_length=225, blank=True, null=True)
#     data = models.FileField(upload_to='uploads/', blank=True, null=True)
#     # url = models.URLField(max_length=200)
#     size = models.IntegerField(blank=True, null=True)
#     hash = models.BinaryField()
#     title =  models.CharField(max_length=225, blank=True, null=True)
#     creation = models.DateTimeField(auto_now_add=True)


#     def save(self, *args, **kwargs):
#         self.title = self.data.name
#         extension = self.data.name.split('.')[-1]
#         self.contentType = extension
#         self.size = self.data.size

#         # self.hash = hash_file(encoded)
#         super(Attachment, self).save(*args, **kwargs)

# def hash_file(filename):
#     h = hashlib.md5()
#     with open(filename,'rb') as file:
#         chunk = 0
#         while chunk != b'':
#             chunk = file.read(1024)
#             h.update(chunk).encode('base64').strip()

#     return h.hexdigest()