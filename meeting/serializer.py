from rest_framework import serializers
from .models import Meeting
from .models import Meeting_Participation


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'

class Meeting_ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Participation
        fields = '__all__'