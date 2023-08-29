from django.shortcuts import redirect, render
from django.contrib import messages

def index(request):

    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')


def pricing(request):
    return render(request, '../../leger/templates/pricing.html')