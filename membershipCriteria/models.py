from datetime import date
from django.db import models

from meeting.models import Meeting_Participation
from membersApi.models import Member
from django.db.models.signals import post_save

from officeHours.models import OfficeHour


class MembershipCriteria(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    firstDay_month = models.DateField(verbose_name='Primeiro dia do mês', default=date.today)
    lastDay_month = models.DateField(verbose_name='Último dia do mês', default=date.today)
    officeHoursCriteria = models.DecimalField(verbose_name='Critério de Office Hour')
    meetingsCriteria = models.DecimalField(verbose_name='Critério de Reuniões')
    eventsCriteria = models.DecimalField(verbose_name='Critério de Eventos')

def updateofficeHoursCriteria(instance, **kwargs):
    if OfficeHour.objects.filter(member_id=instance.member, :

        post_save.disconnect(updateofficeHoursCriteria, sender=MembershipCriteria)
        instance.save()

    post_save.connect(updateofficeHoursCriteria, sender=MembershipCriteria)


post_save.connect(updateofficeHoursCriteria, sender=MembershipCriteria)
