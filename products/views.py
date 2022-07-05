from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Product
# Create your views here.

def product_list_view(request):
    all_products = Product.objects.order_by('-created_date')
    paginator = Paginator(all_products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    if 'newest' in request.GET:
        all_products = Product.objects.order_by('-created_date')
        paginator = Paginator(all_products, 3)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        
    elif 'low_price' in request.GET:
        all_products = Product.objects.order_by('price')
        paginator = Paginator(all_products, 3)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        
    elif 'high_price' in request.GET:
        all_products = Product.objects.order_by('-price')
        paginator = Paginator(all_products, 3)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        
    context = {
            'products': products,
            # 'paged_products' : paged_products,
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
