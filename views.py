# from django import views
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
        
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'due_date', 'category']
    search_fields = ['title', 'description']
    
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
       
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    
