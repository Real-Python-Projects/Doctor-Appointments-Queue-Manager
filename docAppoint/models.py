from django.db import models

# Create your models here.


class WaitingPatients(models.Model):
    name = models.CharField(max_length=200)
    issue = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_next = models.BooleanField(default=False)
    in_session = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class AppointmentSession(models.Model):
    person_present = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def timesince(self):
        return self.timestamp.timesince()
    
    def __str__(self):
        return self.person_present
    
class Patients(models.Model):
    name = models.CharField(max_length=100)
    issue = models.TextField()
    time_served = models.DateTimeField()
    
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ["-time_served"]
    
    def __str__(self):
        return self.name