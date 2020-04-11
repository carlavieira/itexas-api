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
        user.nickname = data.get('nickname')
        if data.get('post') != '':
            user.post = data.get('post')
        if data.get('department') != '':
            user.department = data.get('department')
        if data.get('leader') != '':
            user.leader = data.get('leader')
        user.save()
        return user
