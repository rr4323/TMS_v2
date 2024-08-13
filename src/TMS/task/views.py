from django.shortcuts import render
from rest_framework import viewsets
from .models import Tasks
from .serializers import TasksSerializer
import logging
LOGGER = logging.getLogger('django')

class TaskApiViewSet(viewsets.ModelViewSet):
    '''
    Viewset to perform any i.e retrieve,list,.. for a task
    GET /tasks/: Retrieve a list of tasks.
    GET /tasks/<id>/: Retrieve details of a specific task by its ID.
    POST /tasks/: Create a new task.
    PUT /tasks/<id>/: Update an existing task.
    DELETE /tasks/<id>/: Delete a specific task.
    '''
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

