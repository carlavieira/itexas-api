from rest_framework import serializers
from membersApi.models import Member
from .models import Event
from .models import Event_Participation


class ListEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'type', 'member', 'date', 'time', 'url']
        depth = 9


class ManageEventSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Member.objects.all())

    class Meta:
        model = Event
        fields = ['id', 'type', 'member', 'date', 'time', 'url']


class ListEventParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Participation
        fields = ['id', 'member', 'event', 'attendance', 'url']
        depth = 9


class ManageEventParticipationSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Member.objects.all())
    event = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Event.objects.all())

    class Meta:
        model = Event_Participation
        fields = ['id', 'member', 'event', 'attendance', 'url']