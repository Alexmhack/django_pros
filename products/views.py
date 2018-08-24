from django.shortcuts import render

from .models import Product

def product_detail_view(request):
	obj = Product.objects.all()
	context = {
		'object': obj
	}
	return render(request, 'products/detail.html', context)
