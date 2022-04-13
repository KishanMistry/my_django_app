from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import (UserRegisterForm, UserProfileForm)
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
#from user.models import User
from django.conf import settings


def index(request):
    return render(request, 'index.html', {'title':'index'})

def email_send(request):
    # subject = 'Thank you for registering to our site'
    # message = ' it  means a world to us '
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['ksmistry1991@gmail.com',]
    # send_mail( subject, message, email_from, recipient_list)
    # return True    

    subject = 'Subject'
    html_message = render_to_string('user/Email.html', {'username': 'Kishan'})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = 'ksmistry1991@gmail.com'
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            subject, from_email, to = 'welcome', settings.EMAIL_HOST_USER , email
            html_message = render_to_string('user/Email.html', {'username': username})
            plain_message = strip_tags(html_message)
            if (mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)):
                form.save()
                messages.success(request, 'Your account has been created ! You are now able to log in')
                return redirect('login')
            else:
                messages.success(request, 'Fail to send email.')
                return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

def profile(request):
    #, {'context' : context} context = User.objects.filter(user_added=self.request.user)
    form = UserProfileForm(request.POST)
    content = {'form' : form}
    return render(request, 'user/profile.html', content) 