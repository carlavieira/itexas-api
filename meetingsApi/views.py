from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Meeting
from .models import Meeting_Participation
from .serializer import ListMeetingsSerializer, ListMeetingParticipationSerializer
from .serializer import ManageMeetingParticipationSerializer, ManageMeetingSerializer


class ListMeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = ListMeetingsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member',)


class ManageMeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = ManageMeetingSerializer


class ListMeetingParticipationViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Participation.objects.all()
    serializer_class = ListMeetingParticipationSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('meeting', 'member')


class ManageMeetingParticipationViewSet(viewsets.ModelViewSet):
    queryset = Meeting_Participation.objects.all()
    serializer_class = ManageMeetingParticipationSerializer



