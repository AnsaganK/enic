from django.shortcuts import render, get_object_or_404, redirect, reverse

from app.forms import ArticleForm
from app.models import Article
from app.utils import get_paginator, superuser_required


def article_list(request):
    articles = Article.objects.all().order_by('-id')
    articles = get_paginator(request, articles, 6)
    return render(request, 'app/article/list.html', {
        'articles': articles,
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'app/article/detail.html', {
        'article': article,
    })

@superuser_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(reverse('app:article_list'))
    return render(request, 'app/article/create.html')
