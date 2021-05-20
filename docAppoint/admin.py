from django.contrib import admin
from .models import WaitingPatients, AppointmentSession, Patients
# Register your models here.
admin.site.register(WaitingPatients)

@admin.register(AppointmentSession)
class AppointmentSessionAdmin(admin.ModelAdmin):
    list_display=('person_present','timestamp')
    
@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display=('name','time_served')