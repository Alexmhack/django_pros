from django.shortcuts import render

from .models import Product
from .forms import ProductForm

def product_detail_view(request):
	obj = Product.objects.all()
	context = {
		'object': obj
	}
	return render(request, 'products/detail.html', context)


def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, 'products/create.html', context)
