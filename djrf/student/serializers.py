from rest_framework import serializers
from .models import Student
from rest_framework import generics

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'