from django.test import TestCase

from task.models import Tasks
from project.models import Projects
from django.contrib.auth.models import User

class ProjectViewTestCase(TestCase):
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

    def test_project_post_on_valid_data(self):
        valid_project_data={
            "name": "test_project",
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        response= self.client.post("/api/v1/projects/",valid_project_data,content_type='application/json')
        self.assertEquals(response.status_code, 201)
    
    def test_project_post_on_name_is_none(self):
        valid_project_data={
            "name":None,
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        response= self.client.post("/api/v1/projects/",valid_project_data,content_type='application/json')
        self.assertEquals(response.status_code, 400)
    
    def test_project_put_on_valid_data(self):
        valid_project_data={
            "name": "test_project",
            "description": "a put request for project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        response= self.client.put(f"/api/v1/projects/{self.project.id}/",valid_project_data,content_type='application/json')
        self.assertEquals(response.status_code, 200)
    