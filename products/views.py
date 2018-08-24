from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm

def product_detail_view(request):
	obj = Product.objects.all()
	context = {
		'object': obj
	}
	return render(request, 'products/detail.html', context)


def product_create_view(request):
	form = RawProductForm()
	if request.method == "POST":
		form = RawProductForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Product.objects.create(**form.cleaned_data)
		else:
			print(form.errors)
	context = {
		'form': form
	}
	return render(request, 'products/create.html', context)
