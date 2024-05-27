from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import QRForm
from .models import NamostuteQRFormData
import base64
import os
from django.conf import settings
from django.forms.utils import ErrorDict
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone


def home(request):
    return render(request, "pages/namostute-pass.html", {})


def qr_form_view(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            print(name, email, phone_number, address)
            NamostuteQRFormData.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                address=address,
                created_at=timezone.now()
            )
            messages.success(request, 'Form submitted successfully!')
            return redirect('qr_form_view')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors and try again.')
    else:
        form = QRForm()
    return render(request, 'pages/qr-form.html', {'form': form})

    try:
        contact = ContactUsForm.objects.all()
        if request.method == 'POST':
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.phone_number = request.POST.get('mobile')
            contact.message = request.POST.get('message')
            contact.save()

            messages.success(request, 'Message Sent successfully!')
            print(Contact)
            print("success")
            return redirect('contactUs')
        else:
            messages.error(request, 'Something went wrong!')
            return redirect('contactUs')
    except Exception as e:
                messages.error(request, f'Error occurred: {e}')
                return redirect('qr_form_view')