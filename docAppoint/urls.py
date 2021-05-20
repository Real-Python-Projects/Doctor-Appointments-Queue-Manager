from django.urls import path
from .views import IndexView, PatientWaitingCreateView

app_name='mainapp'

urlpatterns = [
    path('', IndexView, name='index'),
    path('add-patients/', PatientWaitingCreateView, name="add-patient"),
]