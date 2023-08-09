from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('employee', 'Employee')])
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # def __init__(self, user, role, avater):
    #     self.user = user
    #     self.role = role
    #     self.avater = avater

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    # def __init__(self, title, description, assigned_to,status):
    #     self.title = title
    #     self.description = description
    #     self.assigned_to = assigned_to

