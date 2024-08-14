from rest_framework import serializers

from .models import Projects
from django.db.models import Q,Count

class ProjectsSerializer(serializers.ModelSerializer):
    '''
    Serializer for Tasks model
    '''

    class Meta:
        model = Projects
        fields = '__all__'

class ProjectProgressSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    def get_progress(self,project):
        task_progress_info=project.tasks.aggregate(
            total_count=Count('id'),
            total_completed=Count('id', filter=Q(status='Completed'))
        )
        if task_progress_info:  
            progress= (task_progress_info['total_completed'] / task_progress_info['total_count'] * 100)
        else:
            progress=0
        return progress
    class Meta:
        model = Projects
        fields = ['progress']