from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import MembershipCriteria
from membersApi.models import Member
from .serializer import MembershipCriteriaSerializer


class MembershipCriteriaViewSet(viewsets.ModelViewSet):
    queryset = MembershipCriteria.objects.all()
    serializer_class = MembershipCriteriaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('member',)


class LedMembershipCriteriaViewSet(viewsets.ModelViewSet):
    serializer_class = MembershipCriteriaSerializer

    def get_queryset(self):
        print(self.request.user.id)
        print(self.request.user)
        return MembershipCriteria.objects.filter(member__leader__id=self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

