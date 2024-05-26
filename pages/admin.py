from django.contrib import admin
from .models import NamostuteQRFormData
from django.contrib import admin

class NamostuteQRFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'created_at')

admin.site.register(NamostuteQRFormData, NamostuteQRFormAdmin)
