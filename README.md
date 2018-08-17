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
