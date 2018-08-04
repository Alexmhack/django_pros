from django.contrib import admin
from django.urls import path

from .views import (
	home_view,
	contact_view,
	contact_confirm_view)

urlpatterns = [
	path('', home_view, name='home'),
	path('contact/', contact_view, name='contact'),
	path('contact/confirm/', contact_confirm_view, name='contact_confirm')
]
