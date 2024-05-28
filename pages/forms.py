from django import forms
from .models import NamostuteQRFormData

class QRForm(forms.ModelForm):
    class Meta:
        model = NamostuteQRFormData
        fields = ['name', 'email', 'phone_number', 'address']
