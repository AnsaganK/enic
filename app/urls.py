from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    # Pages
    path('', views.home, name='home'),
    path('FAQ', views.faq, name='faq'),

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

    # Contact
    path('contact', views.contact, name='contact'),
    path('contact/messages', views.contact_message_list, name='contact_message_list'),
    path('contact/messages/<int:pk>/json', views.contact_message_json_detail, name='contact_message_json_detail'),
    path('contact/messages/<int:pk>/check', views.contact_message_check, name='contact_message_check'),
    path('api/contact/messages/send', views.contact_message_send, name='contact_message_send'),
    path('api/contact/messages/<str:telegram_id>', views.telegram_contact_messages, name='telegram_contact_messages'),

    # User views
    path('registration', views.registration, name='registration'),
    path('cabinet', views.cabinet, name='cabinet'),

    # University views
    path('university', views.university_list, name='university_list'),
    path('university/map', views.university_map, name='university_map'),
    path('university/<str:region_id>/json', views.region_universities, name='region_universities'),
    # path('news', views.news_list, name='news_list'),
    # path('news/<slug:slug>', views.news_detail, name='news_detail'),
    # path('contact', views.contact, name='contact'),
    # path('cabinet', views.cabinet, name='cabinet'),
]
