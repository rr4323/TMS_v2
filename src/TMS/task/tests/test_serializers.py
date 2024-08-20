from django.test import TestCase

from task.models import Tasks
from project.models import Projects
from django.core.exceptions import ValidationError

class TaskModelSerializerTest(TestCase):

    def setUp(self):
        project_data={
            "name": "test_project",
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        self.project=Projects.objects.create(**project_data)

    def test_valid_task_creation(self):
        valid_task_data={
            "title": "t1",
            "description": "first task",
            "status": "To Do",
            "priority": "Low",
            "due_date": "2024-08-20",
            "project": self.project
        }
        task=Tasks.objects.create(**valid_task_data)
        self.assertTrue(isinstance(task,Tasks))
    
    def test_invalid_task_creation_on_invalid_status(self):
        invalid_task_data={
            "title": "t2",
            "description": "first task",
            "status": "etc", # not a valid status
            "priority": "Low",
            "due_date": "2024-08-20",
            "project": self.project
        }
        with self.assertRaises(ValidationError):
            task = Tasks(**invalid_task_data)
            task.full_clean()

    def test_invalid_task_creation_on_invalid_priority(self):
        invalid_task_data={
            "title": "t2",
            "description": "first task",
            "status": "TO Do", 
            "priority": "etc",# not a valid priority
            "due_date": "2024-08-20",
            "project": self.project
        }
        with self.assertRaises(ValidationError):
            task = Tasks(**invalid_task_data)
            task.full_clean()

    def test_invalid_task_creation_on_invalid_project_id(self):
        invalid_task_data={
            "title": "t2",
            "description": "first task",
            "status": "To Do", 
            "priority": "Low",
            "due_date": "2024-08-20",
            "project_id":3  # not a valid priority
        }
        with self.assertRaises(ValidationError):
            task = Tasks(**invalid_task_data)
            task.full_clean()

    def test_invalid_task_creation_on_invalid_due_date(self):
        invalid_task_data={
            "title": "t2",
            "description": "first task",
            "status": "To Do", 
            "priority": "Low",
            "due_date": "123",# not a valid date
            "project_id":3  
        }
        with self.assertRaises(ValidationError):
            task = Tasks(**invalid_task_data)
            task.full_clean()

    

