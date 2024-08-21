from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from .models import Comments, TaskAssignment, Tasks
from .serializers import CommentsSerializer, TaskAssignmentSerializer, TasksSerializer
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import action
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

    @action(detail=False, methods=['get'])
    def overdue(self, request, *args, **kwargs):
        
        today=datetime.now()
        overdue_tasks = self.queryset.filter(Q(due_date__lt=today) & ~Q(status='Completed'))
        serializer = self.serializer_class(overdue_tasks, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class TaskAssignApiViewSet(viewsets.ModelViewSet):

    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer



class TaskUnAssignApiViewSet(viewsets.ModelViewSet):

    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

    def create(self,request,*args,**kwargs):
        LOGGER.info('TaskUnAssignment method is called')
        task_id = request.data.get('task')
        user_id = request.data.get('user')
        try:
            assigned_task=self.queryset.get(task_id=task_id,user_id=user_id)
            assigned_task.delete()
            return Response({'message':'Task is unassigned successfully'},status=status.HTTP_200_OK)
        except TaskAssignment.DoesNotExist as e:
            LOGGER.error('TaskAssignment object does not exist')
            return Response({'error':'TaskAssignment object does not exist'},status=status.HTTP_404_NOT_FOUND)
        
class TaskCommentsApiViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class TaskCommentDeleteApiViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def destroy(self, request, *args, **kwargs):
        #LOGGER.info('comment delete is called')
        comment_id = self.kwargs.get('comment_id')
        try:
            comment = self.queryset.get(id=comment_id)
            comment.delete()
            return Response({'message':'Comment is deleted successfully'},status=status.HTTP_200_OK)
        except Comments.DoesNotExist as e:
            LOGGER.error('Comment object does not exist')
            return Response({'error':'Comment object does not exist'},status=status.HTTP_404_NOT_FOUND)

class TaskCompleteApiViewSet(viewsets.ModelViewSet):

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def update(self,request,*args,**kwargs):
        task_id = self.kwargs.get('id')
        try:
            task=self.queryset.get(id=task_id)
            if task.status == "In Progress":
                task.status='Completed' 
                task.save()
                time_delta=task.updated_at-task.created_at
                LOGGER.info(f"Task completed in {time_delta}")
                return Response({'message':f'Task completed successfully in {time_delta}'},status=status.HTTP_200_OK)
            else:

                return Response({'message':f"Task is at {task.status} so, can't mark as completed"},status=status.HTTP_200_OK)
        except TaskAssignment.DoesNotExist as e:
            LOGGER.error('TaskAssignment object does not exist')
            return Response({'error':'TaskAssignment object does not exist'},status=status.HTTP_404_NOT_FOUND)
        
class TaskOverDueApiViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
    def list(self, request, *args, **kwargs):
        today=datetime.now()
        overdue_tasks = self.queryset.filter(Q(due_date__lt=today) & ~Q(status='Completed'))
        serializer = self.serializer_class(overdue_tasks, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
