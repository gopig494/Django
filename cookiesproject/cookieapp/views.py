from django.shortcuts import render

def cookie(request):
	req=request.COOKIES.get('count',0)
	totalcount=int(req)+1
	dic={'count':totalcount}
	response=render(request,'cookieapp/a.html',context=dic)
	response.set_cookie('count',totalcount)
	return response

# Create your views here.
