from django.shortcuts import render
from . models import Product
from . models import form



# Create your views here.

# def index(request):

#     return render(request,"web/index.html")

def index(request):
        
    dict_prodect = {
        'produ':Product.objects.all(),
    }

    
    if request.method=="POST":
        name=request.POST.get('name')
        message=request.POST.get('message')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        customer = form(
            name=name,
            message=message,
            email=email,
            phone=phone
        )
        customer.save()
    return render(request,'web/index.html',dict_prodect)

def about(request):
    return render(request,"web/about.html")

def brand(request):

    dict_prodect = {
        'produ':Product.objects.all(),
    }    

    return render(request,"web/brand.html",dict_prodect)

def special(request):
    return render(request,"web/special.html")

def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        message=request.POST.get('message')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        customer = form(
            name=name,
            message=message,
            email=email,
            phone=phone,
        )
        customer.save()
    return render(request,"web/contact.html")
