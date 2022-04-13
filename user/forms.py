from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class UserProfileForm(UserCreationForm):
    email = forms.EmailField(max_length = 20, widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder' : 'Enter Email'}))
    phone_no = forms.CharField(max_length = 20, widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder' : 'Enter Phone'}))
    first_name = forms.CharField(max_length = 20, widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder' : 'Enter Name'}))
    last_name = forms.CharField(max_length = 20, widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder' : 'Enter Last Name'}))
    username = forms.CharField(max_length = 20, widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder' : 'Enter Username'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no']