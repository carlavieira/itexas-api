from rest_framework import viewsets
from .models import OfficeHour
from .serializer import OfficeHourSerializer


class OfficeHourViewSet(viewsets.ModelViewSet):
    queryset = OfficeHour.objects.all()
    serializer_class = OfficeHourSerializer