from django.shortcuts import render, redirect
from django.urls import reverse
from ecommerce_app.models import Person
from . import models

# Create your views here.
def mainpage(request):
    return render(request,"ecommerce_app/mainpage.html" )

def loginpage(request):
    if request.POST:
        email = request.POST["email"]
        password = request.POST["password"]
        persons = models.Person.objects.all()
        for person in persons:
            if person.email == email and person.password == password:
                return redirect(reverse("ecommerce_app:storepage"))
            else:
                return render(request,"ecommerce_app/login.html" )
    else:
       return render(request, "ecommerce_app/login.html")

def signuppage(request):
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_again = request.POST["password_again"]
        address = request.POST["address"]
        if password == password_again :
            models.Person.objects.create(name=name, email=email, password=password, 
                                         password_again=password_again, address=address)
        else:
            print("parola uyuşmuyor")
    else:
        print("post yok")
    return render(request,"ecommerce_app/signup.html" )

def storepage(request):
    if request.POST:
        search = request.POST["search"]
        category = models.Product.objects.values('category')
        for i in category:
            for j in i.values():
                if search.lower() in j.lower():
                    product = models.Product.objects.filter(category=j)
        product_dic = {"products":product}            
        return render(request,"ecommerce_app/store.html", context=product_dic)
    else:
        product = models.Product.objects.all()
        product_dic = {"products":product}
        return render(request,"ecommerce_app/store.html", context=product_dic)

def addproductpage(request):
    if request.POST:
        name = request.POST["name"]
        category = request.POST["category"]
        stock = request.POST["stock"]
        price = request.POST["price"]
        image = request.FILES["image"]
        models.Product.objects.create(name=name, category=category, stock=stock, price=price, image=image)
        return redirect(reverse("ecommerce_app:storepage"))
    else:
        return render(request,"ecommerce_app/addproduct.html" )

def sortpage(request):
    if request.POST:
        search = request.POST["search"]
        category = models.Product.objects.values('category')
        for i in category:
            for j in i.values():
                if search.lower() in j.lower():
                    product = models.Product.objects.filter(category=j)
        product_dic = {"products":product}            
        return render(request,"ecommerce_app/store.html", context=product_dic)
    else:
        product = models.Product.objects.all()
        product_dic = {"products":product}
        return render(request,"ecommerce_app/store.html", context=product_dic)
    return render(request, "ecommerce_app/sort.html")