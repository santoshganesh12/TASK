from django.contrib import admin
from .models import Employee, Task

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task)
