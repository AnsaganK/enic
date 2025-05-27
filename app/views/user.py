from django.shortcuts import render


def cabinet(request):
    return render(request, 'app/user/cabinet.html')
