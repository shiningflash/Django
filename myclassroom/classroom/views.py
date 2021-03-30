from django.shortcuts import render
from .models import Student, Teacher, Department
from .serializers import StudentSerializer, TeacherSerializer, DepartmentSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404

class StudentListView(generics.views.APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('New student created...yayy!!!', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetailView(generics.views.APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        student = self.get_object(pk)
        serialize = StudentSerializer(student)
        return Response(serialize.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        student = self.get_object(pk)
        serialize = StudentSerializer(student, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response('Your data updated!! yayyyy...', status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response('Student deleted!!!', status=status.HTTP_204_NO_CONTENT)
    
class TeacherListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class TeacherDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer