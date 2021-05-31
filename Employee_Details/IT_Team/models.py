from django.db import models

# Create your models here.

class empdetails(models.Model):
	EmployeeNo=models.IntegerField()
	EmployeeName=models.CharField(max_length=20)
	EmployeeAddress=models.CharField(max_length=100)
