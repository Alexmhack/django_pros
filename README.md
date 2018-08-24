# django_pros
working with the django 2 tutorial from joincfe.com

```
blank=True | blank=False
null=True | null=False
```

blank=True in a field means we are setting the field to be not required, it will appear as light in
the admin site, and blank=False means this field is required and it will appear bold

null=True means that this field can have a null value in the database, which means that this field 
will be there in database but with a empty value and null=False means this field has to have a value
to be stored in the database.

```
from django.http import HttpResponse
```

We can render raw html on the page using the HttpResponse method, by just wrapping our html with this 
method

```
from django.shortcuts import render
```

We can activate our view using the request that our browser sends when we look for the url, we get 
accept that url using the request arg and render takes in the request, renders our html file and also
a context dict that we can use in our html

```
{{ request.user }} | {{ request.user.is_authenticated }}
```

request is an object that django passes with each url and it has many properties like the user which
tells which is the current user that is accessing the url or we can check if the user is 
authenticated in the admin users, it will return a boolean value.

```
{{ title|title }} | {{ title|capfirst }}
{{ html_context|safe }} | {{ html_context|striptags }}
{{ number|add:50 }}
```

There are a ton of template filter tags that can ease our work in the html itself, we use filters by 
placing a | pipe after the context variable and then using our filter

|add filter adds a number or number in a string to another number context
|title makes the context a title, with capital letter, |capfirst also does the same
|safe is used when we have html tags in the context variable itself and we want html to render
|striptags strips the html tags and only renders the words

# Getting data from database
For getting the data from our database we can use the model objects, we can play around 
with the database model in django shell, run shell using

```
> python manage.py shell
```

Now you can import the model and use the objects to access data

```
>>> from products.models import Product
>>> Product.objects.all()
>>> Product.objects.get(id=1)
```

There are a ton of features that our model objects support which can be found at django2 
docs at official website.

# Django Forms
The module for creating forms in django is the *forms* and we separate our forms by 
creating new file just for our forms

**products/forms.py**
```
from django import forms
```

Their are many ways for creating a form, you can use the model itself for creating one or
just make the form completely fulfilling your requirements

**Model Form in django**
```
from django import forms

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

```

ModelForm class needs a model upon which it can create the form and you have to define the 
fields that the form will have, for all fields use ```fields = "__all__"```

The other way is defining your own fields.

```
from django import forms

class RawProductForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	price = forms.DecimalField()

```

The advantage of using raw fields in our form is that we can use the features of the forms
fields and make our form more nicer looking in html. Some of the features are

```
required=False	 (default is True so we don't mention it in field)
label=''	(default is the name of field but we can override it or just make it empty and use label tags)
attrs={} 	(a dict that can have many key value pair)
```

**products/forms.py**
```
class RawProductForm(forms.Form):
	title = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				"placeholder": "Your Title",
				"class": "form-control",
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

```

In our attrs dictionary we can give a key of "class" which will then be included in our 
input tags as classes of CSS, here we used "form-control" which a mdbootstrap class for 
nicer looking forms. Placholder will give us a nice text displayed in our form.

django.forms does not have a TextField like we have in models so instead of that we use 
widgets in forms.CharField() to render the field as a text field

**products/forms.py**
```
	...
	description = forms.CharField(required=False, widget=forms.Textarea)
	...
```

Either you can just use the default text area made by widget or specify your requirements 
in the Textarea()

**products/forms.py**
```
	...
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
	...
```

There are a lot of fields and widgets in [Django Forms](https://docs.djangoproject.com/en/2.1/ref/forms/fields/)
