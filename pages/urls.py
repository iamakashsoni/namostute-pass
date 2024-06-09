from django.urls import path, include, re_path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='home'),
    path("passes", views.passes, name='passes'),
    path('show_data/', views.show_data, name='show_data'),
    path('download_data/', views.download_data, name='download_data'),
    path('scan-qr-code-@08-06-2024/', views.qr_form_view, name='qr_form_view'),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

