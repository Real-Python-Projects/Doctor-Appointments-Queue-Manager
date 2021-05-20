from django import forms
from .models import WaitingPatients

class PatientWaitingForm(forms.ModelForm):
    class Meta:
        model = WaitingPatients
        exclude = ('is_next','in_session') 