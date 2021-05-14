from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def app(request):
	message='<h1> hi gopi </h2>'
	return HttpResponse(message)
