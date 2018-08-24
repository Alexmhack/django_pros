from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"placeholder": "Your Title",
				"class": "form-control"
			}
		)
	)
	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
				"class": "form-control",
				"rows": 4,
				"cols": 50,
				'placeholder': "Your Description"
			}
		)
	)
	price = forms.DecimalField(initial=299.99)

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]


class RawProductForm(forms.Form):
	title = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"placeholder": "Your Title",
				"class": "form-control"
			}
		)
	)
	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
				"class": "form-control",
				"rows": 4,
				"cols": 50,
				'placeholder': "Your Description"
			}
		)
	)
	price = forms.DecimalField(initial=299.99)
