from rest_framework import serializers
from .models import OfficeHour


class OfficeHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHour
        fields = '__all__'