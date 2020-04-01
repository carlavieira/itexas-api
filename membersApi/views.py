
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):

    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.all()

    def create(self, request, *args, **kwargs):
        created_member = super(MemberViewSet, self).create(request, *args, **kwargs)
        validate_email(self, request.pk)
        return Response({'Message': 'Membro criado!', 'user': created_member})


def validate_email(self, pk):
    print('this is an absurd test '+pk)
    pass
