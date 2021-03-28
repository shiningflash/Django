from django.urls import path
from .views import EmployeeListView, EmployeeDetailsView, DepartmentListView, DepartmentDetailsView


urlpatterns = [
    path('employees', EmployeeListView.as_view()),
    path('employees/<int:pk>', EmployeeDetailsView.as_view()),
    path('departments', DepartmentListView.as_view()),
    path('departments/<int:pk>', DepartmentDetailsView.as_view()),
]