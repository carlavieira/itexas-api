from datetime import date
from django.db import models
from membersApi.models import Member
from departmentApi.models import Department
from postApi.models import Post

class Meeting(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Início', default=date.today)
    end_date = models.DateField(verbose_name='Término', default=date.today)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Cargo')
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Área')

class Meeting_Participation(models.Model):
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, verbose_name='Reunião')
    attendance = models.BooleanField(default=False, verbose_name='Presença')