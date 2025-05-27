from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),

    # About urls
    path('about', views.about, name='about'),
    path('about/strategy', views.about_strategy, name='about_strategy'),
    path('about/structure', views.about_structure, name='about_structure'),
    path('about/memorandum', views.about_memorandum, name='about_memorandum'),
    path('about/social-life', views.about_social_life, name='about_social_life'),

    # Article urls
    path('article', views.article_list, name='article_list'),
    path('article/create', views.article_create, name='article_create'),
    path('article/<slug:slug>', views.article_detail, name='article_detail'),

    # Pages
    path('contact', views.contact, name='contact'),
    path('FAQ', views.faq, name='faq'),

    # User views
    path('registration', views.registration, name='registration'),
    path('cabinet', views.cabinet, name='cabinet'),

    # path('news', views.news_list, name='news_list'),
    # path('news/<slug:slug>', views.news_detail, name='news_detail'),
    # path('contact', views.contact, name='contact'),
    # path('cabinet', views.cabinet, name='cabinet'),
]
