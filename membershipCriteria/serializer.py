from rest_framework import serializers
from .models import MembershipCriteria


class MembershipCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipCriteria
        fields = '__all__'
        depth = 9
