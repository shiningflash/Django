from django.db import models

# name, address, registered_at, updated_at

class UserBaseModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'users'
        ordering = ['registered_at', 'name']


class Department(models.Model):
    department_id = models.CharField(max_length=200)
    department_name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    
    def __str__(self):
        return f'{self.department_id} - {self.department_name}'
    
    class Meta:
        db_table = 'departments'
        ordering = ['department_id']
        
class Student(UserBaseModel):
    student_id = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.student_id} - {self.name}'
    
    class Meta:
        db_table = 'students'
        
class Teacher(UserBaseModel):
    teacher_id = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.teacher_id} - {self.name}'
    
    class Meta:
        db_table = 'teachers'