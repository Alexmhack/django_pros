from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})


def about_view(request):
	context = {
		"title": "About Django Store",
		"number": 500,
		"html": "<h1>Sample HTML</h1>"
	}
	return render(request, 'about.html', context)
