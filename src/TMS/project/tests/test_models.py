from django.test import TestCase
from project.models import Projects
from django.core.exceptions import ValidationError
from random import randint

class TaskModelTest(TestCase):

    def test_valid_project_creation(self):
        valid_project_data={
            "name": "test_project",
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        project=Projects.objects.create(**valid_project_data)
        self.assertTrue(isinstance(project,Projects))
    
    def test_invalid_project_creation_on_name_is_none(self):
        invalid_project_data={
            "name": None,
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        with self.assertRaises(ValidationError):
            task = Projects(**invalid_project_data)
            task.full_clean()

    def test_invalid_project_creation_on_invalid_date(self):
        invalid_project_data={
            "name": "test_project",
            "description": "a test project to assign task to it",
            "start_date": "123",
            "end_date": "234"
            }
        with self.assertRaises(ValidationError):
            task = Projects(**invalid_project_data)
            task.full_clean()

   
