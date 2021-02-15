from django.urls import path, include
from .views import ShowStudent

urlpatterns = [
    path('', ShowStudent.as_view()),
]