from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=50000)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.title} - {self.created}'
        
class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.voter} - {self.post.title}'