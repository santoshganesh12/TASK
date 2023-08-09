from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes,  authentication_classes
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user.employee)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'access': user.auth_token.key})
    else:
        return Response({'detail': 'Invalid credentials'}, status=400)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Make sure to import TokenAuthentication
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'detail': 'Logged out successfully.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'detail': 'This is a protected view.'})



@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'detail': 'Username and password are required.'}, status=400)

    try:
        user = User.objects.create_user(username, password=password)
        return Response({'detail': 'User registered successfully.'}, status=201)
    except Exception as e:
        return Response({'detail': str(e)}, status=500)
    
class EmployeeList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmployeeDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class TaskList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TaskDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
