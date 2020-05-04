from datetime import date
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from membersApi.models import Member


class MembershipCriteria(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    dayMonth = models.DateField(verbose_name='Dia do mês', default=date.today)
    officeHoursCriteria = models.DecimalField(verbose_name='Critério de Office Hour', max_digits=5, decimal_places=2)
    meetingsCriteria = models.DecimalField(verbose_name='Critério de Reuniões', max_digits=5, decimal_places=2)
    eventsCriteria = models.DecimalField(verbose_name='Critério de Eventos', max_digits=5, decimal_places=2)
    status = models.TextField(verbose_name='Status', default='-')


@receiver(post_save, sender=MembershipCriteria)
def updateStatus(instance, **kwargs):
    if instance.officeHoursCriteria < 80 or instance.meetingsCriteria < 75 or instance.eventsCriteria < 50:
        print('Entrou na condição de risco')
        instance.status = "RISCO"
        post_save.disconnect(updateStatus, sender=MembershipCriteria)
        instance.save()

    if instance.officeHoursCriteria >= 80 and instance.meetingsCriteria >= 75 and instance.eventsCriteria >= 50:
        print('Entrou na condição de ideal')
        instance.status = "IDEAL"
        post_save.disconnect(updateStatus, sender=MembershipCriteria)
        instance.save()

    post_save.connect(updateStatus, sender=MembershipCriteria)
