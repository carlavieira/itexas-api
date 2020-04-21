from datetime import date
from django.db import models
from membersApi.models import Member
from departmentsApi.models import Department
from postsApi.models import Post


class Background(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Início', default=date.today)
    end_date = models.DateField(verbose_name='Término', default=date.today)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Cargo')
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Área')