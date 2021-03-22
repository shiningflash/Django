from django.urls import path
from .views import StudentListView, StudentDetailsView, StudentCreateView, StudentList

urlpatterns = [
    path('students', StudentListView.as_view()),
    path('students/<int:pk>', StudentDetailsView.as_view()),
    path('students/create', StudentCreateView.as_view()),
    path('students/filter', StudentList.as_view()),
]