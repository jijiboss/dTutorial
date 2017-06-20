from django.contrib import admin
from .models import Suppliers, Products, Orders

admin.site.register(Suppliers)
admin.site.register(Products)
admin.site.register(Orders)
