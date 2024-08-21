from django.test import TestCase

from task.models import Tasks
from project.models import Projects
from django.contrib.auth.models import User

class TaskViewTestCase(TestCase):
    def setUp(self):
        project_data={
            "name": "test_project",
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        self.project=Projects.objects.create(**project_data)
        task_data={
            "title": "t1",
            "description": "first task",
            "status": "To Do",
            "priority": "Low",
            "due_date": "2024-08-20",
            "project": self.project
        }
        self.task=Tasks.objects.create(**task_data)
        self.user=User.objects.create(username="test_user")

    def test_task_get(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEquals(response.status_code, 200)
        
    def test_task_post_on_valid_data(self):
        #post test case for tasks
        valid_task_data={
            "title": "t1",
            "description": "first task",
            "status": "To Do",
            "priority": "Low",
            "due_date": "2024-08-20",
            "project": self.project.id
        }
        response = self.client.post('/api/v1/tasks/',valid_task_data, content_type='application/json')
        self.assertEquals(response.status_code, 201)

    def test_task_post_on_invalid_data(self):
        #post test case for tasks
        invalid_task_data={
            "title": "t1",
            "description": "first task",
            "status": "To D",#this is invalid
            "priority": "Low",
            "due_date": "2024-08-20",
            "project": self.project.id
        }
        response = self.client.post('/api/v1/tasks/',invalid_task_data, content_type='application/json')
        self.assertEquals(response.status_code, 400)

    def test_task_put_on_invalid_data(self):
        #put test case for tasks
        invalid_task_data={
            "title": "t1",
            "description": "first task",
            "status": "To D",#this is invalid
            "priority": "Low",
            "due_date": "2024-08-20",
            "project": self.project.id
        }
        response = self.client.put(f'/api/v1/tasks/{self.task.id}/',invalid_task_data, content_type='application/json')
        self.assertEquals(response.status_code, 400)
      
    def test_task_put_on_valid_data(self):
        #put test case for tasks
        valid_task_data={
            "title": "t1",
            "description": "first task",
            "status": "To Do",
            "priority": "Low",
            "due_date": "2024-08-20",
            "project": self.project.id
        }
        response = self.client.put(f'/api/v1/tasks/{self.task.id}/',valid_task_data, content_type='application/json')
        self.assertEquals(response.status_code, 200)
      
    def test_task_assign_post_on_invalid_data(self):
        #post test case for assign tasks
        invalid_task_data={
            "user": self.user.id,
            "task": 3
            }
        response = self.client.post(f'/api/v1/tasks/{self.task.id}/assign/',invalid_task_data, content_type='application/json')
        self.assertEquals(response.status_code, 400)

    def test_task_assign_post_on_valid_data(self):
        #post test case for assign tasks
        valid_task_data={
            "user": self.user.id,
            "task": self.task.id
            }
        response = self.client.post(f'/api/v1/tasks/{self.task.id}/assign/',valid_task_data, content_type='application/json')
        self.assertEquals(response.status_code, 201)
