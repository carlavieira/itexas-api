from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializer import DepartmentSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
