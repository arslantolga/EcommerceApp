from django.contrib import admin
from ecommerce_app.models import Person, Product
from . import models

# Register your models here.

admin.site.register(Person)
admin.site.register(Product)
