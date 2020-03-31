from rest_framework import viewsets
from .models import Meeting
from .models import Meeting_Participation
from .serializer import MeetingSerializer
from .serializer import Meeting_ParticipationSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class Meeting_ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Participation.objects.all()
    serializer_class = Meeting_ParticipationSerializer