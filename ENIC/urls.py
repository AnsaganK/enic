from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as acc
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
]

urlpatterns += [
    path('login', acc.LoginView.as_view(), name='login'),
    path('logout', acc.LogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
