from django.shortcuts import render
from django.http import HttpResponse 

def gm(a):
	return HttpResponse ("Hi buddy Good Morning")

def gf(b):
	return HttpResponse ("Hi buddy Good Afternoon")


def ge(c):
	return HttpResponse ("Hi buddy Good Evening")
# Create your views here.
