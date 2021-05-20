from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, timedelta
from .models import AppointmentSession

@receiver(post_save, sender=WaitingPatients)
def appointment_expiry(sender, instance, created, **kwargs):
    if created:
        AppointmentSession.apply_async(
            args=(instance.pk),
            eta=datetime.utcnow()+timedelta(minutes=2)
        )