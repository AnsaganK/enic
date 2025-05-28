from django.shortcuts import render, get_object_or_404

from app.forms import ArticleForm
from app.models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'app/article/list.html', {
        'articles': articles,
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'app/article/detail.html', {
        'article': article,
    })


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm()
        pass
