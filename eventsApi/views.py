from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Event
from .models import Event_Participation
from .serializer import ListEventSerializer, ManageEventSerializer
from .serializer import ListEventParticipationSerializer, ManageEventParticipationSerializer


class ListEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = ListEventSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member',)


class ManageEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = ManageEventSerializer


class ListEventParticipationViewSet(viewsets.ModelViewSet):
    queryset = Event_Participation.objects.all()
    serializer_class = ListEventParticipationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('event', 'member',)


class ManageEventParticipationViewSet(viewsets.ModelViewSet):
    queryset = Event_Participation.objects.all()
    serializer_class = ManageEventParticipationSerializer
