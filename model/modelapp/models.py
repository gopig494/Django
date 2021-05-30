from django.db import models

# Create your models here.
class list(models.Model):
	RollNo=models.IntegerField()
	StudentName=models.CharField(max_length=20)
	
