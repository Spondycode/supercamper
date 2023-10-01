from django.shortcuts import render
from .forms import RegisterForm

def home(request):
    return render(request, 'main/home.html' )


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, 'registration/sign_up.html', context)
