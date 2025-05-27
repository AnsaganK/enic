from django.shortcuts import render


def home(request):
    return render(request, 'app/page/home.html')


def faq(request):
    return render(request, 'app/page/FAQ.html')
