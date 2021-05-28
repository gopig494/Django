from django.shortcuts import render

def session(request):
	req=request.session.get('count',0)
	totalcount=int(req)+1
	#dic={'count':totalcount}
	request.session ['count']=totalcount
	return render(request, 'sessionapp/a.html',{'count':totalcount})

# Create your views here.
