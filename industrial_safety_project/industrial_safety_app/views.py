from django.shortcuts import render
from rest_framework import viewsets,permissions

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]


def index(request):
    return render(request, 'main/index.html')


def about(request):
    tasks = Task.objects.all()
    return render(request, 'main/about.html', {'tasks': tasks})
