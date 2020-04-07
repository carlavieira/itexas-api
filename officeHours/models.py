from datetime import date
from django.db import models
from django.utils import timezone
from membersApi.models import Member
from django.db.models.signals import post_save


class OfficeHour(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Dia', default=date.today)
    checkin_time = models.DateTimeField(verbose_name='Hora do check-in', default=timezone.now)
    checkout_time = models.DateTimeField(verbose_name='Hora do check-out', blank=True, null=True)
    duration = models.DurationField(verbose_name='Duração', blank=True, null=True, help_text='[HH:[MM:] format')


def updateOfficeHourDuration(instance, **kwargs):
    if instance.checkin_time and instance.checkout_time:
        instance.duration = instance.checkout_time - instance.checkin_time
        post_save.disconnect(updateOfficeHourDuration, sender=OfficeHour)
        instance.save()

    post_save.connect(updateOfficeHourDuration, sender=OfficeHour)


post_save.connect(updateOfficeHourDuration, sender=OfficeHour)
