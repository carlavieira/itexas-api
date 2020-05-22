from rest_framework import serializers
from .models import Background
from departmentsApi.models import Department
from postsApi.models import Post
from membersApi.models import Member


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ['id', 'member', 'start_date', 'end_date', 'post', 'department', 'description' ]
        depth = 9

class ManageBackgroundSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(required=True, many=False,
                                                    read_only=False, queryset=Member.objects.all())
    post = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                              read_only=False, queryset=Post.objects.all())
    department = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                                    read_only=False, queryset=Department.objects.all())
    class Meta:
        model = Background
        fields = ['id', 'member', 'start_date', 'end_date', 'post', 'department', 'description' ]
        depth = 9