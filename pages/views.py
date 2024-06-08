from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import QRForm
from .models import NamostuteQRFormData
from django.utils import timezone
import json

def home(request):
    #return render(request, "pages/namostute-pass.html", {})
    return render(request, "pages/thankyou-page.html", {})

def pass(request):
    return render(request, "pages/namostute-pass.html", {})
    #return render(request, "pages/thankyou-page.html", {})


def qr_form_view(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            qr_data = NamostuteQRFormData.objects.filter(
                name=data['name'],
                email=data['email'],
                phone_number=data['phone_number'],
                address=data['address']
            ).first()

            if qr_data:
                if qr_data.is_QRscanned:
                    messages.error(request, 'This QR code has already been used.')
                    return redirect('qr_form_view')
                else:
                    qr_data.is_QRscanned = True
                    qr_data.save()
                    messages.success(request, 'QR code scanned successfully!')
                    return redirect('qr_form_view')
            else:
                NamostuteQRFormData.objects.create(
                    name=data['name'],
                    email=data['email'],
                    phone_number=data['phone_number'],
                    address=data['address'],
                    created_at=timezone.now(),
                    is_QRscanned=True
                )
                messages.success(request, 'Form submitted successfully!')
                return redirect('qr_form_view')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors and try again.')
    else:
        form = QRForm()
    return render(request, 'pages/qr-form.html', {'form': form})
