from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-@naadvenu-2018/', admin.site.urls),
    path("", include("pages.urls")),

]
