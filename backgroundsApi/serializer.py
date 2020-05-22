from rest_framework import serializers
from .models import Background
from departmentsApi.models import Department
from postsApi.models import Post


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ['id', 'member', 'start_date', 'end_date', 'post', 'department', 'description' ]
        depth = 9

class ManageBackgroundSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                              read_only=False, queryset=Post.objects.all())
    department = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                                    read_only=False, queryset=Department.objects.all())
    class Meta:
        model = Background
        fields = ['id', 'member', 'start_date', 'end_date', 'post', 'department', 'description' ]
        depth = 9