from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'pages/home.html')

def about_page_view(request):
    return render(request, 'pages/about.html')

def contact_page_view(request):
    return render(request, 'pages/contact.html')
