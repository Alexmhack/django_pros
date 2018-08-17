from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
	return HttpResponse("<h2>HOME PAGE VIEW</h2>")


def contact_view(request, *args, **kwargs):
	return HttpResponse("<h2>CONTACT VIEW</h2>")
