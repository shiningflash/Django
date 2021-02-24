from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.filters import SearchFilter, OrderingFilter

from . import models
from . import serializers


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('student_id', 'fullname', 'address')