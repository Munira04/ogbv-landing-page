from django import forms
from .models import IncidentReport

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['incident_type', 'platform', 'description', 'contact_info']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
            'incident_type': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'platform': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'contact_info': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Optional'}),
        }