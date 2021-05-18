from django.db import models

# Create your models here.

class gopi(models.Model):
	name=models.CharField(max_length=20)
	no=models.IntegerField()
	salary=models.IntegerField()