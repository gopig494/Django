from django.shortcuts import render
from django.http import HttpResponse
import datetime

def t(a):
	return HttpResponse('<h1>Hi the time is :'+str(datetime.datetime.now())+'</h1>')