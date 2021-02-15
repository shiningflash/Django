from django.db import models

class Student(models.Model):
    studentid = models.AutoField(auto_created=True, primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstname