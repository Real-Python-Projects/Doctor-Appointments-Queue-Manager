from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import AppointmentSession
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
    return "Item Deleted"
