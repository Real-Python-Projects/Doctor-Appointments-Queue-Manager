from django.contrib import admin
from .models import WaitingPatients, AppointmentSession
# Register your models here.
admin.site.register(WaitingPatients)
admin.site.register(AppointmentSession)