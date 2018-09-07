from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import ProductForm, RawProductForm

def product_detail_view(request, id):
	object = get_object_or_404(Product, id=id)
	context = {
		'object': object
	}
	return render(request, 'products/detail.html', context)


def product_list_view(request):
	products = Product.objects.all()
	context = {
		'products': products
	}
	return render(request, 'products/list.html', context)


def product_create_view(request):
	initial_data = {
		'title': 'ASUS Laptop',
		'description': 'Cheapest laptop with great features'
	}
	form = ProductForm(request.POST or None, initial=initial_data)
	if request.method == "POST":
		if form.is_valid():
			print(form.cleaned_data)
			Product.objects.create(**form.cleaned_data)
		else:
			print(form.errors)
	context = {
		'form': form
	}
	return render(request, 'products/create.html', context)


def product_delete_view(request, id):
	obj = get_object_or_404(Product, id)
	if request.method == "POST":
		obj.delete()
	context = {
		'object': obj
	}
	return render(request, 'products/delete.html', context)
