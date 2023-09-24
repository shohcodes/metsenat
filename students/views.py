from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from students.filters import StudentTypeFilter, StudentInstituteFilter
from students.models import Student
from students.serializers import StudentSerializer, StudentCreateSerializer, StudentUpdateSerializer, \
    StudentListSerializer, StudentDetailSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [StudentTypeFilter, StudentInstituteFilter]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'create':
            return StudentCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return StudentUpdateSerializer
        elif self.action == 'list':
            return StudentListSerializer
        elif self.action == 'retrieve':
            return StudentDetailSerializer
        return self.serializer_class
