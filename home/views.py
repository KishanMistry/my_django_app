#from curses.ascii import HT
from django.shortcuts import (get_object_or_404, render, redirect ,HttpResponseRedirect)
from home.models import Product
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from home.form import ProductForm

# Create your views here.
def index(request):
    posts_list = Product.objects.all().order_by('id')    
    query = request.GET.get('q')
    if query:
        posts_list = Product.objects.filter(
            Q(product_name__icontains=query) | Q(price__icontains=query)
        ).distinct()
    paginator = Paginator(posts_list, 3) # 6 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,        
    }
    return render(request, "index.html", context)
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
    per_page = 6
    obj_paginator = Paginator(products, per_page)   
    first_page = obj_paginator.page(1).object_list   
    page_range = obj_paginator.page_range
    context = {
        'obj_paginator':obj_paginator,
        'products':first_page,
        'page_range':page_range
    }
    
    if request.method == 'POST' and 'page_no' in request.POST:
        page_no = request.POST.get('page_no', None) 
        results = list(obj_paginator.page(page_no).object_list.values('id', 'product_name','price', 'available_quantity', 'image'))
        return JsonResponse({"results":results})
    return render(request, 'product.html', context)

def contact(request):
    return render(request, 'contact.html')

def edit_product(request,id):
    context ={}
    obj = get_object_or_404(Product, id = id)
    form = ProductForm(request.POST or None, request.FILES or None,instance = obj) 
    if form.is_valid():
        form.save()
        messages.success(request, 'Product updated successfully!')            
        return redirect('product')
    
    # add form dictionary to context
    context["form"] = form
    return render(request, 'product_edit.html', context)

def delete_product(request, id):
    if request.method == 'POST':
        dl = Product.objects.get(pk=id)
        dl.delete()
        messages.success(request, 'Deleted Successfully!')
        return redirect('/product')