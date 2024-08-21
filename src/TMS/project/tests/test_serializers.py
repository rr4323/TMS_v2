from django.test import TestCase

from project.serializers import ProjectsSerializer

class ProjectModelSerializerTest(TestCase):

    def test_valid_project_creation(self):
        valid_project_data={
            "name": "test_project",
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        project=ProjectsSerializer(data=valid_project_data)
        self.assertTrue(project.is_valid())
    
    def test_invalid_project_creation_on_name_is_none(self):
        valid_project_data={
            "name":None,
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        project=ProjectsSerializer(data=valid_project_data)
        self.assertFalse(project.is_valid())


    def test_invalid_project_creation_on_invalid_date(self):
        valid_project_data={
            "name":"test_project",
            "description": "a test project to assign task to it",
            "start_date": "123",
            "end_date": "456"
            }
        project=ProjectsSerializer(data=valid_project_data)
        self.assertFalse(project.is_valid())


    