from django.db import models

class IncidentReport(models.Model):
    INCIDENT_TYPES = [
        ('doxing', 'Doxing'),
        ('cyberstalking', 'Cyber Stalking'),
        ('cyberbullying', 'Cyber Bullying'),
        ('non_consensual', 'Non-Consensual Image Sharing'),
        ('other', 'Other')
    ]
    
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    platform = models.CharField(max_length=100, help_text="Where did this occur? (e.g., WhatsApp, X, Facebook)")
    description = models.TextField()
    contact_info = models.CharField(max_length=255, blank=True, null=True, help_text="Optional: Leave blank to remain anonymous")
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_type} reported on {self.reported_at.strftime('%Y-%m-%d')}"