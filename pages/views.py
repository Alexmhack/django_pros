from django.shortcuts import render
from django.http import HttpResponse

def home_view(*args, **kwargs):
	return HttpResponse("<h2>HOME PAGE VIEW</h2>")


def contact_view(*args, **kwargs):
	return HttpResponse("<h2>CONTACT VIEW</h2>")
