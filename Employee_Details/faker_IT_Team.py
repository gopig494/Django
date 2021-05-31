import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Employee_Details.settings')


import django 
django.setup()

from random import randint
from IT_Team.models import empdetails
from faker import Faker
faker=Faker()

def pop(n):
    for i in range(n):
        no=randint(1,50)
        name=faker.name()
        address=faker.city()
        rec=empdetails.objects.get_or_create(EmployeeNo=no,EmployeeName=name,EmployeeAddress=address)
pop(51)