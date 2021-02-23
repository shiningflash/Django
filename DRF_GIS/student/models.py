from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=8)
    fullname = models.CharField(max_length=255)
    cgpa = models.FloatField()
    contact_no = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.student_id  
