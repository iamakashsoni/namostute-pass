from django.urls import path, include, re_path
from pages import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("", views.home, name='home'),
    path('scan-qr-code-@08-06-2024/', views.qr_form_view, name='qr_form_view'),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^uploads/(?P<path>.)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
