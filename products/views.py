from django.shortcuts import render, get_object_or_404

from .models import Product
# Create your views here.

def product_list_view(request):
    products = Product.objects.order_by('-created_date')
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)

def product_detail_view(request, pk):
    single_product = get_object_or_404(Product, pk=pk)
    products = Product.objects.order_by('-created_date')
    context = {
        'single_product': single_product,
        'products': products,
    }
    return render(request, 'products/product_detail.html', context)
