from django.shortcuts import render
from . import form

# Create your views here.

def details(request):
	details=form.students()
	dic={'det':details}
	return render(request,'formapp/a.html',context=dic)