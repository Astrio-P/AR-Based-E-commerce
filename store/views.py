from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    """
    This method is used to view the registration page.
    """
    if request.user.is_authenticated:
        return redirect ('store')
    
    else:
        form= CreateUserForm()
         
        if request.method == 'POST' :
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request, 'Account created successfully. Please login to continue ' + user)
                
                return redirect('login')
                
        context= {'form': form}
        return render(request, 'store/register.html', context)


def loginPage(request):
    """
    This method is used to view the login page.
    """
    if request.user.is_authenticated:
        return redirect('store')
    else:
          if request.method == 'POST':
              username =request.POST.get('username')
              password =request.POST.get('password')
             
              user= authenticate(request, username=username, password=password)

              if user is not None:
                  login(request, user)
                  return redirect('store')
              else:
                  messages.info(request, 'Username or Password is incorrect')
            

    context= {}
    return render(request, 'store/login.html', context)

def logoutUser(request):
    """
    This method is used to logout the user and redirect them to the login page.
    """
    logout(request)
    return redirect('login')

def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)