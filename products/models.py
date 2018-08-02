from django.db import models


class Product(models.Model):
	title = models.TextField()
	description = models.TextField()
	price = models.TextField()
	summary = models.TextField(default='This is cool!')