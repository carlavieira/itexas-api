from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import OfficeHour
from .serializer import ListOfficeHourSerializer, ManageOfficeHourSerializer


class ListOfficeHourViewSet(viewsets.ModelViewSet):
    queryset = OfficeHour.objects.all()
    serializer_class = ListOfficeHourSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member', 'date')


class ManageOfficeHourViewSet(viewsets.ModelViewSet):
    queryset = OfficeHour.objects.all()
    serializer_class = ManageOfficeHourSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member', 'date')
