from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import AppointmentSession, WaitingPatients, Patients
from celery import shared_task
from time import sleep
from django.utils import timezone
from django.contrib import messages

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/30')),
    name="end_consultation",
    ignore_result=True
)
def end_patient_consultation():
    model = AppointmentSession.objects.last()
    if model is not None:
        model.delete()
    next_patient = WaitingPatients.objects.last()
    if next_patient is not None:
        messages.info(request, f"{{ next_patient.name }} you are up")
        AppointmentSession.objects.create(person_present=next_patient.name)
        Patients.objects.create(name=next_patient.name,
                                issue=next_patient.issue,
                                time_served=timezone.now())
        next_patient.delete()
    messages.info(request, "No more patients")
    return "Item Deleted"
