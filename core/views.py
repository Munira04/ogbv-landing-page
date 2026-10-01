from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncidentReportForm

def home(request):
    return render(request, 'core/index.html')

def report_incident(request):
    return redirect('https://gbv-system.onrender.com/report/')

def services(request):
    return render(request, 'core/services.html')

def types(request):
    return render(request, 'core/types.html')