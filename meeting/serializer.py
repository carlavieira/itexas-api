from rest_framework import serializers
from membersApi.models import Member
from .models import Meeting
from .models import Meeting_Participation


class MeetingSerializer(serializers.ModelSerializer):
    member = serializers.SlugRelatedField(many=False, read_only=False, slug_field='first_name',
                                          queryset=Member.objects.all())

    class Meta:
        model = Meeting
        fields = ('type', 'member', 'date', 'time')


class Meeting_ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Participation
        fields = '__all__'
