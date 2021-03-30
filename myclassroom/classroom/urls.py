from django.urls import path
from .views import StudentListView, StudentDetailView, TeacherListView, TeacherDetailsView

urlpatterns = [
    path('api/students', StudentListView.as_view()),
    path('api/students/<int:pk>', StudentDetailView.as_view()),
    path('api/teachers', TeacherListView.as_view()),
    path('api/teachers/<int:pk>', TeacherDetailsView.as_view()),
]
