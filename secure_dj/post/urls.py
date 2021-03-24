from django.urls import path
from .views import PostView, PostCreateView

urlpatterns = [
    path('post/create', PostCreateView.as_view()),
    path('post', PostView.as_view()),
]
