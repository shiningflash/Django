from .models import Post
from django.contrib.auth import get_user_model
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        
        created_at = serializers.DateTimeField(format='%a, %d %b %Y')
        author = serializers.SlugRelatedField(
            queryset=get_user_model().objects.all(), slug_field='username'
        )