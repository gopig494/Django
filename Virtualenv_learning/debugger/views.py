from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def debugger_view(request):
    a = request.GET.get("info")
    value = callme()
    return HttpResponse("debugger working")

def callme():
    values = []
    for k in range(100):
        for m in range(k):
            values.append(m)
    return values
