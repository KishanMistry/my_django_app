#from curses.ascii import HT
from django.shortcuts import render, HttpResponse
from home.models import Product
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    context = { "variable" : "This is the variable" }
    return render(request, 'index.html', context) 
    #return HttpResponse("This is home page")    

def about(request):
    return render(request, 'about.html')

def product(request):
    success = 0
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        available_quantity = request.POST.get('available_quantity')
        price = request.POST.get('price')
        file_url = ''
        if request.FILES['image']:
            image = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(image.name, image)
            file_url = fss.url(file)
        date = datetime.today()
        product = Product(product_name = product_name, available_quantity = available_quantity, price = price, image = file_url, date = date)
        if product.save():
            success = 1
            return render(request, 'product.html', {'success': 1})
    return render(request, 'product.html', {'success': success})

def contact(request):
    return render(request, 'contact.html')
