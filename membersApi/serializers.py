from django.utils import timezone
from departmentApi.models import Department
from postApi.models import Post
from .models import Member
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    getPosts = Post.objects.all()
    postChoices = [(choice.id, choice.name) for choice in getPosts]
    getDepartments = Department.objects.all()
    departmentChoices = [(choice.id, choice.name) for choice in getDepartments]
    getLeaders = Member.objects.filter(post=2)
    leaderChoices = [(choice.id, choice.first_name) for choice in getLeaders]
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=100)
    post = serializers.ChoiceField(postChoices)
    department = serializers.ChoiceField(departmentChoices)
    leader = serializers.ChoiceField(leaderChoices)
    slack = serializers.CharField(required=False, max_length=50)
    phone = serializers.CharField(required=False, max_length=20)
    nickname = serializers.CharField(required=False, max_length=30)
    photo = serializers.ImageField(required=False)
    date_joined = serializers.DateTimeField(required=False, default=timezone.now())

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'photo': self.validated_data.get('photo', ''),
            'slack': self.validated_data.get('slack', ''),
            'phone': self.validated_data.get('phone', ''),
            'post': self.validated_data.get('post', ''),
            'department': self.validated_data.get('department', ''),
            'leader': self.validated_data.get('leader', ''),
            'date_joined': self.validated_data.get('date_joined', ''),
        }


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id', 'email', 'first_name', 'last_name', 'post', 'department', 'leader', 'photo', 'slack', 'phone',
            'nickname', 'date_joined', 'is_active', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}
