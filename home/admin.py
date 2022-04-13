from django.contrib import admin
from home.models import Product

class AdminProduct(admin.ModelAdmin):
    model = Product
    list_display = ('product_name', 'available_quantity', 'price')

admin.site.register(Product, AdminProduct)