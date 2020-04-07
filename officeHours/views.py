from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import OfficeHour
from .serializer import OfficeHourSerializer


class OfficeHourViewSet(viewsets.ModelViewSet):
    queryset = OfficeHour.objects.all()
    serializer_class = OfficeHourSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member', 'date')
