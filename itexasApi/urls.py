
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from membersApi.views import MemberViewSet
from departmentsApi.views import DepartmentViewSet
from postsApi.views import PostViewSet
from officeHoursApi.views import OfficeHourViewSet
from backgroundsApi.views import BackgroundViewSet
from meetingsApi.views import MeetingViewSet
from meetingsApi.views import Meeting_ParticipationViewSet
from eventsApi.views import EventViewSet
from eventsApi.views import Event_ParticipationViewSet
from membershipCriteria.views import MembershipCriteriaViewSet

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'officeHoursApi', OfficeHourViewSet)
router.register(r'backgroundsApi', BackgroundViewSet)
router.register(r'meetingsApi', MeetingViewSet)
router.register(r'meeting_participation', Meeting_ParticipationViewSet)
router.register(r'eventsApi', EventViewSet)
router.register(r'event_participation', Event_ParticipationViewSet)
router.register(r'membershipCriteria', MembershipCriteriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
