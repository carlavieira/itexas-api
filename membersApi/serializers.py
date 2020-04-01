from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('email', 'first_name', 'last_name', 'post', 'department', 'leader', 'photo', 'slack', 'phone',
                  'is_staff')

        extra_kwargs = {'password': {'write_only': True}}
