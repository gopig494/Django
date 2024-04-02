from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def debugger_view(request):
    a = request.GET.get("info")
    value = callme()
    return render(request,"dubugger/index.html",{'value':value})

def callme():
    values = []
    for k in range(100):
        for m in range(k):
            values.append(m)
    return values
