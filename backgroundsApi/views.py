from rest_framework import viewsets
from .models import Background
from .serializer import BackgroundSerializer, ManageBackgroundSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ListBackgroundViewSet(viewsets.ModelViewSet):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member',)

class ManageBackgroundViewSet(viewsets.ModelViewSet):
    queryset = Background.objects.all()
    serializer_class = ManageBackgroundSerializer