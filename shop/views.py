from django.shortcuts import render
from .models import *
from .forms import ProductForm

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'product_list.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return ProductForm('users_list')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form':form})



def product(request,product_id):
    print(product_id)
    prod = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product':prod})