from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import QRForm
from .models import NamostuteQRFormData
from django.utils import timezone
import json
from django.http import HttpResponse
import csv


def home(request):
    #return render(request, "pages/namostute-pass.html", {})
    return render(request, "pages/thankyou-page.html", {})

def passes(request):
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

def show_data(request):
    data = NamostuteQRFormData.objects.all()
    return render(request, 'pages/show_data.html', {'data': data})

def download_data(request):
    data = NamostuteQRFormData.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="qr_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone Number', 'Address', 'Created At'])
    for item in data:
        writer.writerow([item.name, item.email, item.phone_number, item.address, item.created_at])

    return response