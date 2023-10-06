from django.contrib import admin
from .models import Category, Customer, Product, Order
from main.models import Profile


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
# admin.site.register(Profile)
