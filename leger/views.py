from django.shortcuts import redirect, render
from django.contrib import messages

def home(request):

    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')


def pricing(request):
    return render(request, '../../leger/templates/pricing.html')

def index2(request):
    return render(request, 'index2.html')

