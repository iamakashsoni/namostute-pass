from django.urls import path, include, re_path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='home'),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

