from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from app.forms import RegisterForm


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('app:home')
        else:
            print(form.errors)
    return render(request, 'registration/registration.html')
