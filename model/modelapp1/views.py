from django.shortcuts import render
from modelapp1.models import list

# Create your views here.
def secondapp(request):
	db=list.objects.all()
	dic={'db':db}
	return render (request,'modelapp1/b.html',context=dic)
