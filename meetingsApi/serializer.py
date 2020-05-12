from membersApi.models import Member
from .models import Meeting
from .models import Meeting_Participation
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ListMeetingsSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'type', 'member', 'date', 'time', 'engagement', 'url')
        depth = 3

class ManageMeetingSerializer(ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Member.objects.all())

    class Meta:
        model = Meeting
        fields = ('id', 'type', 'member', 'date', 'time', 'engagement', 'url')
        depth = 3


class ManageMeetingParticipationSerializer(ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Meeting.objects.all())
    member = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Member.objects.all())

    class Meta:
        model = Meeting_Participation
        fields = ['id', 'meeting', 'member', 'attendance', 'url']
        unique_together = ('member', 'meeting')
        depth = 3


class ListMeetingParticipationSerializer(ModelSerializer):
    class Meta:
        model = Meeting_Participation
        fields = ['id', 'meeting', 'member', 'attendance', 'url']
        depth = 3
