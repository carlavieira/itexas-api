from rest_framework import viewsets
from .models import Background
from .serializer import BackgroundSerializer


class BackgroundViewSet(viewsets.ModelViewSet):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer