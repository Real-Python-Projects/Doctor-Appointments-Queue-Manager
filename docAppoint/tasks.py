from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import AppointmentSession
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def end_patient_consultation(pk):
    try:
        AppointmentSessions.objects.get(pk=pk).delete()
    except AppointmentSessions.DoesNotExist:
        pass
