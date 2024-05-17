from django.db import models

# Create your models here.
class Employee(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Photo=models.ImageField(upload_to='images')
    Designation=models.CharField(max_length=100)
    Email_address=models.EmailField(max_length=100)
    Phone_Number=models.CharField(max_length=10,unique=True)
    def _str_(self):
        return self.First_Name