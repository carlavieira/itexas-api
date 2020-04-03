from allauth.account.adapter import DefaultAccountAdapter

from departmentApi.models import Department
from membersApi.models import Member
from postApi.models import Post


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.slack = data.get('slack')
        user.phone = data.get('phone')
        user.post = Post.objects.get(id=data.get('post'))
        user.department = Department.objects.get(id=data.get('department'))
        user.leader = Member.objects.get(id=data.get('leader'))
        user.save()
        return user
