#from curses.ascii import HT
from django.shortcuts import render, HttpResponse
from home.models import Product
from datetime import datetime
# Create your views here.
def index(request):
    context = { "variable" : "This is the variable" }
    return render(request, 'index.html', context) 
    #return HttpResponse("This is home page")    

def about(request):
    return render(request, 'about.html')

def product(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        available_quantity = request.POST.get('available_quantity')
        price = request.POST.get('price')
        image = request.POST.get('image')
        date = datetime.today()
        product = Product(product_name = product_name, available_quantity = available_quantity, price = price, image = image, date = date)
        product.save()
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')
