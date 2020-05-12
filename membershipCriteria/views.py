from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import MembershipCriteria
from .serializer import MembershipCriteriaSerializer


class MembershipCriteriaViewSet(viewsets.ModelViewSet):
    queryset = MembershipCriteria.objects.all()
    serializer_class = MembershipCriteriaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member',)
