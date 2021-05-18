from django.shortcuts import render
import datetime

def gopi(request):
	date=datetime.datetime.now()
	hr=int(date.strftime('%H'))
	if hr>12:
		msg="Hi Good evening"
	elif hr==12:
		msg="Hi Good afternoon"
	else:
		msg="Hi Good morning"
		
	dic={'time':date,'name':'gopi','wish':msg}
	return render(request,"gopi/a.html", context=dic)




# Create your views here.
