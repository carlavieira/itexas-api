from rest_framework import serializers
from .models import OfficeHour


class OfficeHourSerializer(serializers.ModelSerializer):
    checkin_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    checkout_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    date = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = OfficeHour
        fields = '__all__'
