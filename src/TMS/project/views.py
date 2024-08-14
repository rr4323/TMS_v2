from django.shortcuts import render
from rest_framework import viewsets
from .models import Projects
from .serializers import ProjectProgressSerializer, ProjectsSerializer
from rest_framework import status
from rest_framework.response import Response
import logging
LOGGER = logging.getLogger('django')

class ProjectApiViewSet(viewsets.ModelViewSet):
    '''
    Viewset to perform any i.e retrieve,list,.. for a task
    GET /projects/: Retrieve a list of tasks.
    GET /projects/<id>/: Retrieve details of a specific task by its ID.
    POST /projects/: Create a new task.
    PUT /projects/<id>/: Update an existing task.
    DELETE /projects/<id>/: Delete a specific task.
    '''
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ProjectProgressApiViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectProgressSerializer

    def retrieve(self, request, *args, **kwargs):
        project_id=kwargs.get('id')
        try:
            project = Projects.objects.get(id=project_id)
        except Projects.DoesNotExist as e:
            LOGGER.error(e)
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer=self.serializer_class(project)
            return Response(serializer.data,status=status.HTTP_200_OK)
            
        


        