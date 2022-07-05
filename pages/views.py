from django.core.mail import send_mail
from django.shortcuts import redirect, render

from accounts.models import CustomUser
from products.models import Product
from contact.models import Contact
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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        email_subject = 'New Email from ClothingShop website regarding: '+ subject
        email_body = 'Name: '+ name +'\nEmail: '+ email +'\n\nMessage:\n'+ message
        admin_info = CustomUser.objects.get(is_superuser=True, username='admin')

        send_mail(
            email_subject,
            email_body,
            's.talebi.sut@gmail.com',
            [admin_info.email],
            fail_silently=False,
        )
        return redirect('contact')

    return render(request, 'pages/contact.html')
