from django.utils import timezone
from departmentsApi.models import Department
from postsApi.models import Post
from .models import Member
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    def update(self, instance, validated_data):
        super(CustomRegisterSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        super(CustomRegisterSerializer, self).create(validated_data)

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(required=False)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=100)
    post = serializers.PrimaryKeyRelatedField(
        required=False, many=False, read_only=False, queryset=Post.objects.all())
    department = serializers.PrimaryKeyRelatedField(
        required=False, many=False, read_only=False, queryset=Department.objects.all())
    leader = serializers.PrimaryKeyRelatedField(
        required=False, many=False, read_only=False, queryset=Member.objects.filter(post=2))
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
            'nickname': self.validated_data.get('nickname', ''),
            'date_joined': self.validated_data.get('date_joined', ''),
        }


class MemberSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Post.objects.all().filter(),
    )
    department = serializers.SlugRelatedField(
        required=False,
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Department.objects.all()
    )
    leader = serializers.SlugRelatedField(
        required=False,
        many=False,
        read_only=False,
        slug_field='first_name',
        queryset=Member.objects.filter(post=2)
    )

    class Meta:
        model = Member
        fields = (
            'id', 'templates', 'first_name', 'last_name', 'post', 'department', 'leader', 'photo', 'slack', 'phone',
            'nickname', 'date_joined', 'is_active', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}
