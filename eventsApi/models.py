from django.core.exceptions import ObjectDoesNotExist
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
    engagement = models.DecimalField(verbose_name='Engajamento', max_digits=5, decimal_places=2, default=0)


class Event_Participation(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Evento')
    attendance = models.BooleanField(default=False, verbose_name='Presença')


@receiver(post_save, sender=Event_Participation)
def updateEventParticipationCriteria(instance, **kwargs):
    try:
        criteria_to_update: MembershipCriteria = MembershipCriteria.objects.filter(
            member_id=instance.member.id,
            dayMonth__month=instance.event.date.month
        ).get()
    except ObjectDoesNotExist:
        criteria_to_update = MembershipCriteria(member=instance.member, dayMonth=instance.event.date,
                                                officeHoursCriteria=0, meetingsCriteria=0, eventsCriteria=0)

    all_events: int = Event.objects.filter(
        date__month=instance.event.date.month
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

@receiver(post_save, sender=Event_Participation)
def updateEngagement(instance, **kwargs):
    event_to_update: Event = Event.objects.filter(id=instance.event_id).get();
    present: int = Event_Participation.objects.filter(
        event=event_to_update, attendance=True
    ).count()
    total: int = Event_Participation.objects.filter(
        event=event_to_update
    ).count()
    event_to_update.engagement = (present / total) * 100
    event_to_update.save()


@receiver(post_save, sender=Event)
def create_participation(sender, instance, created, **kwargs):
    if created:
        for member in Member.objects.all().filter(is_active=True):
            Event_Participation.objects.create(member=member, event=instance, attendance=False);
