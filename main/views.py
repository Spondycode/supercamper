from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html' )


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, 'registration/sign_up.html', context)




def pass_reset(request):
    # context = {"form": form}
    return render(request, 'password_reset.html')
