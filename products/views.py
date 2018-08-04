from django.shortcuts import render

from .forms import ContactForm

def contact(request):
	contact_form = ContactForm()
	return render(request, 'contact_form.html', {'contact_form': contact_form})