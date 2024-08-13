from rest_framework import serializers

from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    '''
    Serializer for Tasks model
    '''

    class Meta:
        model = Projects
        fields = '__all__'
