from django.db import models

class UserBaseModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['registered_at',]
        db_table = 'users'
        
    def __str__(self):
        return self.name
    
    
class Department(models.Model):
    department_id = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    
    class Meta:
        ordering = ['department_id', 'name',]
        db_table = 'departments'
        
    def __str__(self):
        return f'({self.department_id}, {self.name})'
    

class Employee(UserBaseModel):
    employee_id = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'employees'
        
    def __str__(self):
        return f'({self.employee_id}, {self.name})'
    
    
class Customer(UserBaseModel):
    customer_id = models.CharField(max_length=200, unique=True)
    
    class Meta:
        db_table = 'customers'
        
    def __str__(self):
        return f'({self.customer_id}, {self.name})'
    
    