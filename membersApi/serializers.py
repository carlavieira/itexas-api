from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields= ('email', 'first_name', 'last_name', 'nickname', 'post', 'department', 'leader', 'photo', 'slack', 'phone')
        extra_kwargs = {'password': {'write_only': True}}
