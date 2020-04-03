from rest_framework import serializers
from .models import Event
from .models import Event_Participation


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class Event_ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Participation
        fields = '__all__'