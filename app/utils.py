from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def superuser_required(view_func):
    return user_passes_test(
        lambda u: u.is_superuser,
        login_url='/'
    )(view_func)

def get_paginator(request, queryset, count=12):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return queryset