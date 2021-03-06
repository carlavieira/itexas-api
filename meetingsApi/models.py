from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from membersApi.models import Member
from membershipCriteria.models import MembershipCriteria
from django.db.models.signals import post_save
from django.dispatch import receiver


class Meeting(models.Model):
    MEETINGS = (('REB', 'REB'), ('RA', 'Reunião de Área'), ('RT', 'Reunião de Time'), ('LR', 'Reunião de LR'),
                ('CN', 'Reunião de Corner'))
    type = models.CharField(max_length=3, choices=MEETINGS, blank=True, null=True, verbose_name='Tipo da Reunião')
    member = models.ForeignKey(Member, verbose_name='Responsável', on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='Dia')
    time = models.TimeField(verbose_name='Hora')
    engagement = models.DecimalField(verbose_name='Engajamento', max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.type + ' ' + str(self.date) + ' ' + str(self.time)


class Meeting_Participation(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name='Reunião')
    attendance = models.BooleanField(default=False, verbose_name='Presença')


@receiver(post_save, sender=Meeting_Participation)
def updateMeetingParticipationCriteria(instance, **kwargs):

    try:
        criteria_to_update = MembershipCriteria.objects.filter(
            member_id=instance.member.id,
            dayMonth__month=instance.meeting.date.month
        ).get()
    except ObjectDoesNotExist:
        criteria_to_update = MembershipCriteria(member=instance.member, dayMonth=instance.meeting.date,
                                                officeHoursCriteria=0, meetingsCriteria=0, eventsCriteria=0)

    all_meetings = Meeting_Participation.objects.filter(
        member_id=instance.member.id,
        meeting__date__month=instance.meeting.date.month
    ).count()

    all_attended_meetings = Meeting_Participation.objects.filter(
        member_id=instance.member.id,
        meeting__date__month=instance.meeting.date.month,
        attendance=True
    ).count()

    criteria_to_update.meetingsCriteria = (all_attended_meetings/all_meetings)*100

    print('Todas as reuniões: ' + str(all_meetings))
    print('Todas as meetings participadas: ' + str(all_attended_meetings))
    print('Porcentagem: ' + str(criteria_to_update.meetingsCriteria))
    criteria_to_update.save()

@receiver(post_save, sender=Meeting_Participation)
def updateEngagement(instance, **kwargs):
    meeting_to_update: Meeting = Meeting.objects.filter(id=instance.meeting_id).get();
    present: int = Meeting_Participation.objects.filter(
        meeting=meeting_to_update, attendance=True
    ).count()
    total: int = Meeting_Participation.objects.filter(
        meeting=meeting_to_update
    ).count()
    meeting_to_update.engagement = (present / total) * 100
    meeting_to_update.save()

@receiver(post_save, sender=Meeting)
def create_participation(sender, instance, created, **kwargs):
    if created:
        Meeting_Participation.objects.create(member=instance.member, meeting=instance, attendance=True);