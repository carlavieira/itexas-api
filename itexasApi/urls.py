
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
from django.urls import include, path
from rest_framework import routers

from membersApi.views import MemberViewSet, UpdateMemberViewSet
from departmentsApi.views import DepartmentViewSet
from postsApi.views import PostViewSet
from officeHoursApi.views import ListOfficeHourViewSet, ManageOfficeHourViewSet
from backgroundsApi.views import BackgroundViewSet
from meetingsApi.views import ListMeetingViewSet, ManageMeetingViewSet
from meetingsApi.views import ListMeetingParticipationViewSet, ManageMeetingParticipationViewSet
from eventsApi.views import ListEventViewSet, ManageEventViewSet
from eventsApi.views import ListEventParticipationViewSet, ManageEventParticipationViewSet
from membershipCriteria.views import MembershipCriteriaViewSet

router = routers.DefaultRouter()
router.register(r'list-members', MemberViewSet)
router.register(r'manage-member', UpdateMemberViewSet)
router.register(r'manage-departments', DepartmentViewSet)
router.register(r'manage-posts', PostViewSet)
router.register(r'list-office-hours', ListOfficeHourViewSet)
router.register(r'manage-office-hours', ManageOfficeHourViewSet)
router.register(r'list-backgrounds', BackgroundViewSet)
router.register(r'list-meetings', ListMeetingViewSet)
router.register(r'manage-meetings', ManageMeetingViewSet)
router.register(r'list-meeting-participation', ListMeetingParticipationViewSet)
router.register(r'manage-meeting-participation', ManageMeetingParticipationViewSet)
router.register(r'list-events', ListEventViewSet)
router.register(r'manage-event', ManageEventViewSet)
router.register(r'list-event-participation', ListEventParticipationViewSet)
router.register(r'manage-event-participation', ManageEventParticipationViewSet)
router.register(r'list-membership-criteria', MembershipCriteriaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
