from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import AppointmentSession, WaitingPatients
from celery import shared_task

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="end_consultation",
    ignore_result=True
)
def end_patient_consultation():
    model = AppointmentSession.objects.last()
    model.delete()
    next_patient = WaitingPatients.objects.last()
    AppointmentSession.objects.create(person_present=next_patient)
    return "Item Deleted"
