from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def report_incident(request):
    return render(request, 'core/report.html')

def services(request):
    return render(request, 'core/services.html')

def types(request):
    return render(request, 'core/types.html')