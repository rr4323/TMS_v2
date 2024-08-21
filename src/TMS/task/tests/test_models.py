from django.test import TestCase

from task.models import Comments, TaskAssignment, Tasks
from project.models import Projects
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from random import randint

class TaskModelTest(TestCase):

    def setUp(self):
        project_data={
            "name": "test_project",
            "description": "a test project to assign task to it",
            "start_date": "2024-08-20T18:37:51.040Z",
            "end_date": "2024-08-20T18:37:51.040Z"
            }
        self.project=Projects.objects.create(**project_data)
        self.invalid_project_id = randint(self.project.id+1,self.project.id+100)

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
            "project_id":self.invalid_project_id  # not a valid priority
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
            "project":self.project
        }
        with self.assertRaises(ValidationError):
            task = Tasks(**invalid_task_data)
            task.full_clean()



class TaskAssignmentModelTest(TestCase):

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
        self.user=User.objects.create(username="test_user")
        self.task=Tasks.objects.create(**task_data)
        self.invalid_task_id = randint(self.task.id+1,self.task.id+10)
        self.invalid_user_id =  randint(self.user.id+1,self.user.id+10)

    def test_valid_task_assignment(self):
        valid_task_data={
            "user":self.user,
            "task": self.task
        }
        task=TaskAssignment.objects.create(**valid_task_data)
        self.assertTrue(isinstance(task,TaskAssignment))
    
    def test_invalid_task_assignment_on_invalid_user(self):
        invalid_task_data={
            "user_id":self.invalid_user_id,
            "task": self.task
        }
        with self.assertRaises(ValidationError):
            task = TaskAssignment(**invalid_task_data)
            task.full_clean()

    def test_invalid_task_assignment_on_invalid_project(self):
        invalid_task_data={
            "user":self.user,
            "task_id":self.invalid_task_id
        }
        with self.assertRaises(ValidationError):
            task = TaskAssignment(**invalid_task_data)
            task.full_clean()

    

class TaskCommentModelTest(TestCase):

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
        self.user=User.objects.create(username="test_user")
        self.task=Tasks.objects.create(**task_data)
        self.invalid_task_id = randint(self.task.id+1,self.task.id+10)
        self.invalid_user_id =  randint(self.user.id+1,self.user.id+10)

    def test_valid_task_comment(self):
        valid_task_data={
            "user":self.user,
            "task": self.task,
            "text": "this is a comment"
        }
        task=Comments.objects.create(**valid_task_data)
        self.assertTrue(isinstance(task,Comments))
    
    def test_invalid_task_comment_on_invalid_user(self):
        invalid_task_data={
            "user_id":self.invalid_user_id,
            "task": self.task,
            "text": "this is a comment"
        }
        with self.assertRaises(ValidationError):
            task = Comments(**invalid_task_data)
            task.full_clean()

    def test_invalid_task_comment_on_invalid_task(self):
        invalid_task_data={
            "user":self.user,
            "task_id":self.invalid_task_id,
            "text":"this is a comment"
        }
        with self.assertRaises(ValidationError):
            task = Comments(**invalid_task_data)
            task.full_clean()

    def test_invalid_task_comment_on_comment_is_none(self):
        invalid_task_data={
            "user":self.user,
            "task_id":self.invalid_task_id,
            "text":None
        }
        with self.assertRaises(ValidationError):
            task = Comments(**invalid_task_data)
            task.full_clean()

    


