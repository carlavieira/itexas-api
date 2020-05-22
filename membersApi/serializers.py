from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from datetime import date
from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from departmentsApi.models import Department
from postsApi.models import Post
from .models import Member
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
import random
import string
import time


def mkpass(size=16):
    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    # chars.extend([i for i in '\'"!@#$%&*()-_=+[{}]~^,<.>;:/?'])
    passwd = ''
    for i in range(size):
        passwd += chars[random.randint(0, len(chars) - 1)]
        random.seed = int(time.time())
        random.shuffle(chars)

    return passwd


class CustomRegisterSerializer(RegisterSerializer):
    def update(self, instance, validated_data):
        super(CustomRegisterSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        super(CustomRegisterSerializer, self).create(validated_data)

    def validate(self, data):
        send_mail(
            'Senha de acesso iTexas',  # aqui colocamos o assunto
            'Aqui está sua senha de acesso: ' + data['password1'],  # aqui vai o corpo do email
            'belohorizonte@aiesec.org.br',  # email que vai ser exibido teoricamente
            [data['email'], ]
        )
        return data

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(default=mkpass(16), required=False)
    password2 = password1
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=100)
    post = serializers.PrimaryKeyRelatedField(
        required=False, many=False, read_only=False, queryset=Post.objects.all(), allow_null=True)
    department = serializers.PrimaryKeyRelatedField(
        required=False, many=False, read_only=False, queryset=Department.objects.all(), allow_null=True)
    leader = serializers.PrimaryKeyRelatedField(
        required=False, many=False, read_only=False, queryset=Member.objects.all(), allow_null=True)
    slack = serializers.CharField(required=False, max_length=50, allow_null=True, allow_blank=True)
    phone = serializers.CharField(required=False, max_length=20, allow_null=True, allow_blank=True)
    nickname = serializers.CharField(required=False, max_length=30, allow_null=True, allow_blank=True)
    photo = serializers.ImageField(required=False, allow_null=True)
    date_joined = serializers.DateField(required=False, default=date.today(), allow_null=True)

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


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id', 'email', 'first_name', 'last_name', 'post', 'department', 'leader', 'photo', 'slack', 'phone',
            'nickname', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
        depth = 9


class UpdateMemberSerializer(ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                              read_only=False, queryset=Post.objects.all())
    department = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                                    read_only=False, queryset=Department.objects.all())
    leader = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                                read_only=False, queryset=Member.objects.all())
    photo = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = Member
        fields = (
            'id', 'email', 'first_name', 'last_name', 'post', 'department', 'leader', 'photo', 'slack', 'phone',
            'nickname', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}


class PasswordResetSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm

    def validate_email(self, value):
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(_('Error'))

        ###### FILTER YOUR USER MODEL ######
        if not Member.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))
        return value

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),

            ###### USE YOUR TEXT FILE ######
            'email_template_name': 'password_reset_email.html',

            'request': request,
        }
        self.reset_form.save(**opts)
