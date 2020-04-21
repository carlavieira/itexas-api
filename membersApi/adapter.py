from allauth.account.adapter import DefaultAccountAdapter

from departmentsApi.models import Department
from membersApi.models import Member
from postsApi.models import Post


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.slack = data.get('slack')
        user.phone = data.get('phone')
        if data.get('post') != '':
            user.post = Post.objects.get(id=data.get('post'))
        if data.get('department') != '':
            user.department = Department.objects.get(id=data.get('department'))
        if data.get('leader') != '':
            user.leader = Member.objects.get(id=data.get('leader'))
        user.save()
        return user
