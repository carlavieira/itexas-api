from rest_framework import viewsets
from .models import Background
from .serializer import BackgroundSerializer, ManageBackgroundSerializer


class ListBackgroundViewSet(viewsets.ModelViewSet):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer

class ManageBackgroundViewSet(viewsets.ModelViewSet):
    queryset = Background.objects.all()
    serializer_class = ManageBackgroundSerializer