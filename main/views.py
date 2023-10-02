from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Post


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'main/home.html', context )


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, 'main/create_post.html', context)


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
