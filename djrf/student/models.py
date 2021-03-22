from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = [
            'registered_at',
        ]
        db_table = 'students'
        
    def __str__(self):
        return self.student_id