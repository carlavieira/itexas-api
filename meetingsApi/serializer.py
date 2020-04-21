from rest_framework import serializers
from membersApi.models import Member
from .models import Meeting
from .models import Meeting_Participation


class MeetingSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(many=False,
                                                read_only=False,
                                                queryset=Member.objects.all())

    class Meta:
        model = Meeting
        fields = ('id', 'type', 'member', 'date', 'time', 'url')


class Meeting_ParticipationSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(many=False,
                                                 read_only=False,
                                                 queryset=Meeting.objects.all())

    member = serializers.PrimaryKeyRelatedField(many=False,
                                                read_only=False,
                                                queryset=Member.objects.all())

    class Meta:
        model = Meeting_Participation
        fields = ['id', 'meetingsApi', 'member', 'attendance', 'url']
        unique_together = ('member', 'meetingsApi')
