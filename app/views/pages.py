from django.contrib import messages
from django.shortcuts import render


def home(request):
    return render(request, 'app/page/home.html')


def contact(request):
    return render(request, 'app/page/contact.html')
