from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer, UpdateMemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('post', 'department', 'leader', 'is_active', 'is_staff', 'is_superuser')


class UpdateMemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = UpdateMemberSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('post', 'department', 'leader', 'is_active', 'is_staff', 'is_superuser')

