from rest_framework import routers
from .views import *
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls

urlpatterns = [
    # ... (other URL patterns) ...
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('addemp/', EmployeeList.as_view(), name='emplist'),
    path('viewemp/', EmployeeDetail.as_view(), name='empdetails'),
    path('addtask/', TaskList.as_view(), name='tasklist'),
    path('viewtask/', TaskDetail.as_view(), name='taskdetails'),
]