from django.urls import path, include
from . import views
from django.contrib.auth import views as auth
 
urlpatterns = [
    path('', views.index, name ='index'),
    path("profile/", views.profile, name ='profile'),
    path('login/', views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register/', views.register, name ='register'),

    path('email_send', views.email_send, name ='email_send'),
    
]