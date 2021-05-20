from django.shortcuts import render, reverse
from .forms import PatientWaitingForm
from django.http import HttpResponseRedirect
from .models import WaitingPatients, AppointmentSession
# Create your views here.


def IndexView(request, *args, **kwargs):
    context = {
        "waiting_patients": WaitingPatients.objects.all()
    }
    return render(request, 'index.html', context)

def PatientWaitingCreateView(request, *args, **kwargs):
    
    if request.method == 'POST':
        form = PatientWaitingForm(request.POST)
        
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
     
    content = {
        'form':PatientWaitingForm
     }
    return render(request, 'add_patient.html', content)

def CurrentSession(request, *args, **kwargs):
    context = {
        "current": AppointmentSession.objects.all()
    }
    return render(request, 'current-session.html')