from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from membersApi.models import Member
from membershipCriteria.models import MembershipCriteria


class Event(models.Model):
    EVENTS = (('RG', 'Reunião Geral'), ('AS', 'Assembléia'), ('CF', 'Conferência'), ('OU', 'Outros'))
    type = models.CharField(max_length=3, choices=EVENTS, blank=True, null=True, verbose_name='Tipo do Evento')
    member = models.ForeignKey(Member, verbose_name='Responsável', on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='Dia')
    time = models.TimeField(verbose_name='Hora')


class Event_Participation(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Evento')
    attendance = models.BooleanField(default=False, verbose_name='Presença')


@receiver(post_save, sender=Event_Participation)
def updateMeetingParticipationCriteria(instance, **kwargs):
    criteria_to_update: MembershipCriteria = MembershipCriteria.objects.filter(
        member_id=instance.member.id,
        firstDay_month__month=instance.event.date.month
    ).get()

    all_events: int = Event.objects.filter(
        event__date__month=instance.event.date.month
    ).count()

    all_attended_events: int = Event_Participation.objects.filter(
        member_id=instance.member.id,
        event__date__month=instance.event.date.month,
        attendance=True
    ).count()

    criteria_to_update.eventsCriteria = (all_attended_events / all_events) * 100

    print('Todas os eventos: ' + str(all_events))
    print('Todas os eventos participadas: ' + str(all_attended_events))
    print('Porcentagem: ' + str(criteria_to_update.eventsCriteria))
    criteria_to_update.save()
