from django.contrib import admin
from .models import Profile, Product, Cart, ProductCount

# Register your models here.

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductCount)