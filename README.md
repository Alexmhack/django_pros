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