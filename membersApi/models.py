from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from departmentApi.models import Department
from postApi.models import Post


class Member(AbstractUser):
    username = models.CharField(blank=True, null=True, default=None, max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Cargo')
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Área')
    leader = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Líder')
    photo = models.ImageField(upload_to='uploads', blank=True)
    slack = models.CharField(max_length=255, verbose_name='@Slack')
    phone = models.CharField(max_length=15, verbose_name='Celular')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name