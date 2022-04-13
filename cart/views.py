from django.shortcuts import render, HttpResponse, redirect
from cart.models import Cart
from home.models import Product
#from home.models import Product
from django.contrib import messages
from datetime import datetime
#from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.

def index(request):
    cart = Cart.objects.filter(user_id = request.user.id)
    #return render(request, 'cart_view.html', context) 
    return render(request, 'cart/cart_view.html', {'cart' : cart})   

def add_to_cart(request):
    p_id = request.POST.get('p_id')
    date = datetime.today()
    product = Product.objects.get(pk=p_id)

    if not Cart.objects.filter(user_id = request.user.id, product_id=p_id).exists():
        cart = Cart(product_id = product, user_id= request.user.id, price = product.price, date= date)
        t = cart.save()
        return JsonResponse({"success": True, "message": "Item has been added to cart."})
    else:
        return JsonResponse({"success": False, "message": "Item already in the cart."})
    

def remove_from_cart(request, id):
    if request.method == 'POST':
        dl = Cart.objects.get(pk=id)
        dl.delete()
        messages.success(request, 'Deleted from cart Successfully!')
        return redirect('cart_view')

def update_cart(request, id):
    if request.method == 'POST':
        new_qun = int(request.POST.get('quantity'))
        less = request.POST.get('less')
        more = request.POST.get('more')
        if(less == 'less'):
            new_qun = new_qun - 1
        else:
            new_qun = new_qun + 1
        if(new_qun > 0 ):
            if Cart.objects.filter(pk=id).update(quantity=new_qun):
                messages.success(request, 'Quantity Updated!')
            else:
                messages.success(request, 'Fail to update quantity.')
        else:
            messages.success(request, 'Quantity must be greater than 0.')
        return redirect('cart_view')