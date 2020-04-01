from datetime import date
from django.db import models
from django.utils import timezone
from membersApi.models import Member

class Event(models.Model):
    EVENTS = (('RG', 'Reunião Geral'), ('AS', 'Assembléia'), ('CF', 'Conferência'), ('OU', 'Outros'))
    type = models.CharField(max_length=3, choices=EVENTS, blank=True, null=True, verbose_name='Tipo do Evento')
    member = models.ForeignKey(Member, verbose_name='Responsável', on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='Dia', default=date.today)
    time = models.DateTimeField(verbose_name='Hora', default=timezone.now)

class Event_Participation(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Evento')
    attendance = models.BooleanField(default=False, verbose_name='Presença')