import random
from .models import *
from celery import shared_task
from .utils import auto_assign_tasks

@shared_task
def auto_assign_tasks_task():
    auto_assign_tasks()


def auto_assign_tasks():
    employees = Employee.objects.all()
    tasks = Task.objects.filter(assigned_to=None)

    for task in tasks:
        if employees.exists():
            random_employee = random.choice(employees)
            task.assigned_to = random_employee
            task.save()
            employees = employees.exclude(pk=random_employee.pk)

