from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('post', 'department', 'leader')
    # descobrir se e possivel ter filter e search ao mesmo tempo
    # search_fields = ['first_name', 'last_name', 'phone', 'slack']
