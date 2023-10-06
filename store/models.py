from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# added next line from a comment recommending to take care of plural spelling
    class Meta:
        verbose_name_plural = 'categories'

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100, default='', blank=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places= 2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    # in the description blank means it can be empty and null means it can be missing in action
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    # add On sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __int__(self):
        return self.id


