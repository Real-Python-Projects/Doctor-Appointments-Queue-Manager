from django.contrib import admin
from .models import WaitingPatients, AppointmentSession
# Register your models here.
admin.site.register(WaitingPatients)

@admin.register(AppointmentSession)
class AppointmentSessionAdmin(admin.ModelAdmin):
    list_display=('person_present','timestamp')