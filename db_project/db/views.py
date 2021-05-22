from django.shortcuts import render
from db.models import employee

# Create your views here.

def gp(request):
	data=employee.objects.all()
	alldata={'dataall':data}
	return render (request,'db/a.html',context=alldata)
