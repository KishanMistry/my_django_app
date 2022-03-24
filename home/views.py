#from curses.ascii import HT
from django.shortcuts import render, HttpResponse, redirect
from home.models import Product
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def index(request):
    #context = { "variable" : "This is the variable" }
    posts_list = Product.objects.all()

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
        product.save()
        messages.success(request, 'Product created successfully!')            
    products = Product.objects.all()
    return render(request, 'product.html', {'products' : products})

def contact(request):
    return render(request, 'contact.html')

def edit_product(request,id):
    products = Product.objects.all()
    return render(request, 'product.html',{'id':id, 'products' : products})

def delete_product(request, id):
    if request.method == 'POST':
        dl = Product.objects.get(pk=id)
        dl.delete()
        messages.success(request, 'Deleted Successfully!')            
        return redirect('/product')