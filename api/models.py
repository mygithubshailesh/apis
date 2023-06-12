from django.db import models
from django_otp.models import Device

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()



class Standard(models.Model):
    name = models.CharField(max_length=266)


class Student(models.Model):
    name  = models.CharField(max_length=266)
    age = models.IntegerField()
    Standard = models.ForeignKey(Standard,on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    

