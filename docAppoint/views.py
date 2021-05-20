from django.shortcuts import render, reverse
from .forms import PatientWaitingForm
from django.http import HttpResponseRedirect
# Create your views here.


def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')

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