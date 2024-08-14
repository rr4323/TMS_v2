from rest_framework import serializers

from .models import Comments, TaskAssignment, Tasks

class TasksSerializer(serializers.ModelSerializer):
    '''
    Serializer for Tasks model
    '''

    class Meta:
        model = Tasks
        fields = '__all__'

class TaskAssignmentSerializer(serializers.ModelSerializer):
    '''
    Serializer for Task Assignment model
    '''

    class Meta:
        model = TaskAssignment
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    '''
    Serializer for Task comment model
    '''
    class Meta:
        model = Comments
        fields = '__all__' 