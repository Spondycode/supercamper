# STORE VIEWS.PY

from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm
from django import forms


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, "store.html", context )


def about(request):
    context = {}
    return render(request, 'about.html', context)


# def login_user(request):
#     context = {}
#     return render(request, 'login.html', context)

# def login_user(request):
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			messages.success(request, ("You Have Been Logged In!"))
# 			return redirect('home')
# 		else:
# 			messages.success(request, ("There was an error, please try again..."))
# 			return redirect('login')
#
# 	else:
# 		return render(request, 'login.html', {})
#
#
#
#
#
#
# def logout_user(request):
#     pass
