from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from app.models import Article
from app.models.contact import ContactMessage


class RegisterForm(UserCreationForm):
    username = forms.EmailField(label="Почта")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', 'file', 'telegram_id']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'img', 'content']
