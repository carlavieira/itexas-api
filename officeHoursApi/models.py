from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from membersApi.models import Member
from django.db.models.signals import post_save
from membershipCriteria.models import MembershipCriteria


class OfficeHour(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Dia', default=date.today)
    checkin_time = models.DateTimeField(verbose_name='Hora do check-in', default=timezone.now)
    checkout_time = models.DateTimeField(verbose_name='Hora do check-out', blank=True, null=True)
    duration = models.DurationField(verbose_name='Duração', blank=True, null=True, help_text='[HH:MM]')


def updateOfficeHourDuration(instance, **kwargs):
    if instance.checkin_time and instance.checkout_time:
        instance.duration = instance.checkout_time - instance.checkin_time
        post_save.disconnect(updateOfficeHourDuration, sender=OfficeHour)
        instance.save()

    post_save.connect(updateOfficeHourDuration, sender=OfficeHour)
    criteria_to_update = MembershipCriteria.objects.filter(
        member_id=instance.member.id,
        dayMonth__month=instance.checkin_time.month
    ).get()

    all_office_hours = OfficeHour.objects.filter(
        member_id=instance.member.id,
        checkin_time__month=instance.checkin_time.month
    ).aggregate(Sum('duration'))['duration__sum']

    print(all_office_hours)

    # if all_office_hours > timedelta(hours=20):
    #     criteria_to_update.officeHoursCriteria = 100
    #     criteria_to_update.save()
    # else:
    #     criteria_to_update.officeHoursCriteria = (all_office_hours.seconds / 720) * 100
    #     criteria_to_update.save()

    try:
        criteria_to_update = MembershipCriteria.objects.filter(
            member_id=instance.member.id,
            dayMonth__month=instance.checkin_time.month
        ).get()
    except ObjectDoesNotExist:
        criteria_to_update = MembershipCriteria(member=instance.member, dayMonth=instance.date,
                                                officeHoursCriteria=0, meetingsCriteria=0, eventsCriteria=0)

    all_office_hours = OfficeHour.objects.filter(
        member_id=instance.member.id,
        checkin_time__month=instance.checkin_time.month
    ).aggregate(Sum('duration'))['duration__sum']

    print(all_office_hours)

    if all_office_hours:
        if all_office_hours >= timedelta(hours=20):
            criteria_to_update.officeHoursCriteria = 100
            criteria_to_update.save()
        else:
            criteria_to_update.officeHoursCriteria = (all_office_hours.seconds / 72000) * 100
            criteria_to_update.save()


post_save.connect(updateOfficeHourDuration, sender=OfficeHour)
