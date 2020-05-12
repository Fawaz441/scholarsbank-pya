from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
from django.urls import reverse
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
    uploads = models.IntegerField(default=0)
   
    def __str__(self):
        return self.user.username + " student account "

class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,related_name='seller',null=True,blank=True)
    number = models.CharField(max_length=50)
    whatsapp_number = models.CharField(blank=True,null=True,max_length=50)
    location = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + " seller account "