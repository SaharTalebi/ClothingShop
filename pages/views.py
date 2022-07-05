import imp
from django.shortcuts import render

from products.models import Product
# Create your views here.

def home_page_view(request):
    products = Product.objects.order_by('-created_date')
    context = {
        'products': products
    }
    return render(request, 'pages/home.html', context)

def about_page_view(request):
    return render(request, 'pages/about.html')

def contact_page_view(request):
    return render(request, 'pages/contact.html')
