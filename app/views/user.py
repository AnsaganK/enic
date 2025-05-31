from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from app.forms import UserEditForm
from django.utils.translation import gettext_lazy as _

from app.utils import superuser_required


def cabinet(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.exclude(id=user.id).filter(username=username).exists():
                messages.warning(request, _('Бұл логинмен қолданушы бар. Басқасын таңданыз'))
            else:
                messages.success(request, _('Профиль өзгертілді'))
                form.save()
        return redirect(reverse('app:cabinet'))
    return render(request, 'app/user/cabinet.html')


@superuser_required
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'app/user/list.html', {
        'users': users
    })