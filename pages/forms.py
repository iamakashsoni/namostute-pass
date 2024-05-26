from django import forms

class QRForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)