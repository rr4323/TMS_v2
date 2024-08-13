from rest_framework import serializers

from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    '''
    Serializer for Tasks model
    '''

    class Meta:
        model = Tasks
        fields = '__all__'
