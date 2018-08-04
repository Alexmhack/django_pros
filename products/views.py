from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse

from .forms import ContactForm

def contact_view(request):
	contact_form = ContactForm

	if request.method == "POST":
		form = contact_form(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content
			}

			content = template.render(context)

			email = EmailMessage(
				"New Contact Form Submission",
				content,
				"Your Django App ",
				["pranavg456@gmail.com"],
				headers={'Reply-To': contact_email}
			)

			email.send()
			return render(request, 'contact_confirm.html')

	return render(request, 'contact_form.html', {'contact_form': contact_form})


def home_view(request):
	return HttpResponse("<h1>Home page</h1>")