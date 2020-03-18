from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Member
from .serializers import MemberSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer