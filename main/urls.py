from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create_post', views.create_post, name='create-post'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),),
]
