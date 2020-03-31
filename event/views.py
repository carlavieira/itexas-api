from rest_framework import viewsets
from .models import Event
from .models import Event_Participation
from .serializer import EventSerializer
from .serializer import Event_ParticipationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class Event_ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Event_Participation.objects.all()
    serializer_class = Event_ParticipationSerializer