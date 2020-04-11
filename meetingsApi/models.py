from django.db import models
from django.db.models.signals import post_save

from membersApi.models import Member


class Meeting(models.Model):
    MEETINGS = (('REB', 'REB'), ('RA', 'Reunião de Área'), ('RT', 'Reunião de Time'),
                ('LR', 'Reunião de LR'), ('RC', 'Reunião de Corner'))
    type = models.CharField(max_length=30, choices=MEETINGS, blank=True, null=True, verbose_name='Tipo da Reunião')
    member = models.ForeignKey(Member, verbose_name='Responsável', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(verbose_name='Dia')
    time = models.TimeField(verbose_name='Hora')


class Meeting_Participation(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name='Reunião')
    attendance = models.BooleanField(default=False, verbose_name='Presença')


def meetingParticipationInitiation(instance, **kwargs):
    members = Member.objects.filter(leader=instance.member)
    for member in members:
        m = Meeting_Participation.objects.create(member_id=member.id, meeting_id=instance.id)
        m.save()

#  post_save.connect(updateOfficeHourDuration, sender=Meeting)


post_save.connect(meetingParticipationInitiation, sender=Meeting)
