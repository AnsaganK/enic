from django.shortcuts import render

from app.models import Article


def home(request):
    latest_articles = Article.objects.all().order_by('-created_at')[:3]
    return render(request, 'app/page/home.html', {
        'latest_articles': latest_articles
    })


def faq(request):
    return render(request, 'app/page/FAQ.html')
