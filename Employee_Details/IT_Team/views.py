from django.shortcuts import render
from IT_Team.models import empdetails

# Create your views he

def IT_Team(request):
	db=empdetails.objects.all()
	dic={'db':db}
	return render (request,'IT_Team/index.html',context=dic)
	