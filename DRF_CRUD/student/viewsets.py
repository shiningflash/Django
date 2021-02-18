from rest_framework import viewsets
from rest_framework import permissions

from . import models
from . import serializers


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]