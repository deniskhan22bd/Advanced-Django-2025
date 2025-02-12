import logging 
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend 
from .models import User, Project, Category, Priority, Task
from .serializers import UserSerializer, ProjectSerializer, CategorySerializer, PrioritySerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsAdmin, IsManager, IsEmployee 

logger = logging.getLogger(__name__) 

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data["access"]
            refresh_token = response.data["refresh"]
            res = Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            res.set_cookie(
                key="access_token", 
                value=access_token, 
                httponly=True, 
                secure=True,  # Set to True in production with HTTPS
                samesite="Lax"
            )
            res.set_cookie(
                key="refresh_token", 
                value=refresh_token, 
                httponly=True, 
                secure=True,
                samesite="Lax"
            )
            return res
        return response

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST", "GET"])
def logout_view(request):
    response = Response({"message": "Logged out successfully"})
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin] 

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsManager]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PriorityViewSet(ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['project', 'priority', 'category']
    search_fields = ['title', 'description']
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer): 
        logger.info("Creating a new task") 
        serializer.save()   