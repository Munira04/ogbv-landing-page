from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncidentReportForm

def home(request):
    return render(request, 'core/index.html')

def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your report has been submitted securely and anonymously.')
            return redirect('home')
    else:
        form = IncidentReportForm()
    
    return render(request, 'core/report.html', {'form': form})

def services(request):
    return render(request, 'core/services.html')

def types(request):
    return render(request, 'core/types.html')