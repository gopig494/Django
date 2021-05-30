from django.db import models

# Create your models here.
class list(models.Model):
	EmpNo=models.IntegerField()
	EmpName=models.CharField(max_length=20)
	
