from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=50000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} - {self.text[0:8]}'
    
    class Meta:
        ordering = [
            'created_at',
        ]
        db_table = 'posts'