from .models import Meeting
from .models import Meeting_Participation
from membersApi.serializers import MemberSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class MeetingSerializer(WritableNestedModelSerializer):
    member = MemberSerializer(allow_null=True)

    class Meta:
        model = Meeting
        fields = ('id', 'type', 'member', 'date', 'time', 'url')


class Meeting_ParticipationSerializer(WritableNestedModelSerializer):
    meeting = MeetingSerializer(allow_null=False)

    member = MemberSerializer(allow_null=False)

    class Meta:
        model = Meeting_Participation
        fields = ['id', 'meeting', 'member', 'attendance', 'url']
        unique_together = ('member', 'meeting')
