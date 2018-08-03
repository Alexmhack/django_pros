from django.shortcuts import render
from django.http import HttpResponse

def home_view(*args, **kwargs):
	return HttpResponse("<h2>HOME PAGE VIEW</h2>")