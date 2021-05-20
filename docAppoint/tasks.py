from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="end_consultation",
    ignore_result=True
)
def end_patient_consultation(pk):
    try:
        AppointmentSessions.objects.get(pk=0).delete()
    except AppointmentSessions.DoesNotExist:
        pass
