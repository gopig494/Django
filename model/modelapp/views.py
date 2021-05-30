from django.shortcuts import render
import datetime
from modelapp.models import list

# Create your views here.
def firstapp(request):
	db=list.objects.all()
	ab='welcome'
	cd=datetime.datetime.now()
	dic={'data':ab,
		'data1':cd,
		'db':db}
	return render (request,'modelapp/a.html',context=dic)
