from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=10, null=False, blank=False)
    password_again = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"""
        Name : {self.name}
        Email : {self.email}
        Password : {self.password}
        Password Again : {self.password_again}
        Address : {self.address}
    """

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"""
        Name : {self.name}
        Category : {self.category}
        Stock : {self.stock}
        Price : {self.price}
    """
    
