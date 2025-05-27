from django.shortcuts import render


def about(request):
    return render(request, 'app/about/about.html')


def about_strategy(request):
    return render(request, 'app/about/strategy.html')


def about_structure(request):
    return render(request, 'app/about/structure.html')


def about_memorandum(request):
    return render(request, 'app/about/memorandum.html')


def about_social_life(request):
    return render(request, 'app/about/social_life.html')
