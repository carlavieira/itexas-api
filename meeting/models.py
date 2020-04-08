from django.db import models
from membersApi.models import Member


class Meeting(models.Model):
    MEETINGS = (('REB', 'REB'), ('Reunião de Área', 'Reunião de Área'), ('Reunião de Time', 'Reunião de Time'),
                ('Reunião de LR', 'Reunião de LR'), ('Reunião de Corner', 'Reunião de Corner'))
    type = models.CharField(max_length=30, choices=MEETINGS, blank=True, null=True, verbose_name='Tipo da Reunião')
    member = models.ForeignKey(Member, verbose_name='Responsável', on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='Dia')
    time = models.TimeField(verbose_name='Hora')


class Meeting_Participation(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name='Reunião')
    attendance = models.BooleanField(default=False, verbose_name='Presença')
