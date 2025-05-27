from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from app.forms import ContactMessageForm
from app.models.contact import ContactMessage
from app.service.captcha import verify_recaptcha
from app.utils import superuser_required


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST, request.FILES)
        if form.is_valid():
            token = request.POST.get('g-recaptcha-response')
            if verify_recaptcha(token):
                form.save()
                messages.success(request, 'Жіберілді | Отправлено | Sent')
            else:
                messages.warning(request, 'Recaptcha error')
        else:
            messages.error(request, 'Қате | Ошибка | Error')
        return redirect(reverse('app:contact'))
    return render(request, 'app/contact/contact.html', {
        'site_key': settings.RECAPTCHA_PUBLIC_KEY,
    })


@superuser_required
def contact_message_list(request):
    contact_messages = ContactMessage.objects.all().order_by('-id')
    return render(request, 'app/contact/list.html', {
        'contact_messages': contact_messages,
    })


@superuser_required
def contact_message_json_detail(request, pk):
    contact_message = get_object_or_404(ContactMessage, pk=pk)
    return JsonResponse({
        'name': contact_message.name,
        'subject': contact_message.subject,
        'email': contact_message.email,
        'message': contact_message.message,
        'file': contact_message.file.url if contact_message.file else None,
    })


@superuser_required
def contact_message_check(request, pk):
    contact_message = get_object_or_404(ContactMessage, pk=pk)
    contact_message.is_checked = True
    contact_message.save()
    return redirect(reverse('app:contact_message_list'))
