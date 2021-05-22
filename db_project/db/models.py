from django.db import models
# Create your models here.

class employee(models.Model):
	empno=models.IntegerField()
	empname=models.CharField(max_length=20)
	empsalary=models.IntegerField()
	empaddress=models.CharField(max_length=200)