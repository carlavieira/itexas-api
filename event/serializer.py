from rest_framework import serializers
from membersApi.models import Member
from .models import Event
from .models import Event_Participation


class EventSerializer(serializers.ModelSerializer):
    member = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='first_name',
        queryset=Member.objects.all(),
    )

    class Meta:
        model = Event
        fields = ('id', 'type', 'member', 'date', 'time')


class Event_ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Participation
        fields = '__all__'
