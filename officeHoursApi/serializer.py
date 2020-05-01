from rest_framework import serializers
from .models import OfficeHour
from membersApi.models import Member


class ListOfficeHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHour
        fields = ('id', 'member', 'date', 'checkin_time', 'checkout_time', 'duration', 'url')
        depth = 9


class ManageOfficeHourSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Member.objects.all())

    class Meta:
        model = OfficeHour
        fields = ('id', 'member', 'date', 'checkin_time', 'checkout_time', 'duration', 'url')
