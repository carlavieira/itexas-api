from datetime import date
from django.db import models
from django.utils import timezone
from membersApi.models import Member


class OfficeHour(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Dia', default=date.today)
    checkin_time = models.DateTimeField(verbose_name='Hora do check-in', default=timezone.now)
    checkout_time = models.DateTimeField(verbose_name='Hora do check-out', blank=True, null=True)
    duration = models.DurationField(verbose_name='Duração', blank=True, null=True, help_text='[HH:[MM:] format')