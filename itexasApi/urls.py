
"""itexasApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from membersApi.views import MemberViewSet
from departmentApi.views import DepartmentViewSet
from postApi.views import PostViewSet
from officeHours.views import OfficeHourViewSet
from background.views import BackgroundViewSet
from meeting.views import MeetingViewSet
from meeting.views import Meeting_ParticipationViewSet

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'officeHours', OfficeHourViewSet)
router.register(r'background', BackgroundViewSet)
router.register(r'meeting', MeetingViewSet)
router.register(r'meeting_participation', Meeting_ParticipationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
]
