from django.contrib import admin
from django.urls import path
from cart import views 
urlpatterns = [
    path('cart_view', views.index, name='cart_view'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:id>', views.update_cart, name='update_cart'),
]