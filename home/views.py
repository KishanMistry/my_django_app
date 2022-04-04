#from curses.ascii import HT
from django.shortcuts import render, HttpResponse, redirect
from home.models import Product
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def index(request):
    context = { "variable" : "This is the variable" }
    return render(request, 'index.html', context) 
    #return HttpResponse("This is home page")    

def about(request):
    return render(request, 'about.html')

def product(request):
    if request.method == "POST" and 'page_no' not in request.POST:
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
        product.save()
        messages.success(request, 'Product created successfully!')            
    
    products = Product.objects.all()   
    per_page = 2
    obj_paginator = Paginator(products, per_page)   
    first_page = obj_paginator.page(1).object_list   
    page_range = obj_paginator.page_range

    context = {
    'obj_paginator':obj_paginator,
    'products':first_page,
    'page_range':page_range
    }
    
    if request.method == 'POST':
        page_no = request.POST.get('page_no', None) 
        results = list(obj_paginator.page(page_no).object_list.values('id', 'product_name','price', 'available_quantity', 'image'))
        return JsonResponse({"results":results})
    return render(request, 'product.html', context)

def contact(request):
    return render(request, 'contact.html')

def edit_product(request,id):
    products = Product.objects.all()
    return render(request, 'product.html',{'id':id, 'products' : products })

def delete_product(request, id):
    if request.method == 'POST':
        dl = Product.objects.get(pk=id)
        dl.delete()
        messages.success(request, 'Deleted Successfully!')
        return redirect('/product')
def add_to_cart(request, id):
    try:
        book = Product.objects.get(pk=id)
    except ObjectDoesNotExist:
        pass
    else :
        try:
            cart = Cart.objects.get(user = request.user, active = True)
        except ObjectDoesNotExist:
            cart = Cart.objects.create(user = request.user)
            cart.save()
            cart.add_to_cart(book_id)
            return redirect('cart')
        else:
            return redirect('index')
    return HttpResponse('here')
