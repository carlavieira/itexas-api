from datetime import date
from django.db import models
from membersApi.models import Member


class MembershipCriteria(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    firstDay_month = models.DateField(verbose_name='Primeiro dia do mês', default=date.today)
    lastDay_month = models.DateField(verbose_name='Último dia do mês', default=date.today)
    officeHoursCriteria = models.DecimalField(verbose_name='Critério de Office Hour', max_digits=5, decimal_places=2)
    meetingsCriteria = models.DecimalField(verbose_name='Critério de Reuniões', max_digits=5, decimal_places=2)
    eventsCriteria = models.DecimalField(verbose_name='Critério de Eventos', max_digits=5, decimal_places=2)

