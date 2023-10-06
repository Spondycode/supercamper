# STORE URLS.PY

from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("about/", views.about, name="about"),
    # path("login/", views.login_user, name="login"),
    # path("logout/", views.logout_user, name="logout"),
]
