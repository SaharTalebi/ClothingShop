from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'registration/login.html')

def signup_view(request):
    return render(request, 'registration/signup.html')