
from django import forms
from .models import Product
 
 
# creating a form
class ProductForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Product
 
        # specify fields to be used
        fields = [
            "product_name",
            "available_quantity",
            "price",
            "image"
        ]