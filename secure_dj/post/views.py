from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    