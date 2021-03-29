from django.urls import path
from .views import PostList, PostRetrieveUpdateDestroy, CreateVote

urlpatterns = [
    path('api/posts', PostList.as_view()),
    path('api/posts/<int:pk>', PostRetrieveUpdateDestroy.as_view()),
    path('api/posts/<int:pk>/vote', CreateVote.as_view()),
]