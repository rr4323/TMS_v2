from django.db import models
from django.contrib.auth.models import User

from project.models import Projects


class BaseTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Tasks(BaseTimeStampModel):
    TASK_TYPE=(
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )
    PRIORITY_LEVEL=(
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )
    #project will have multiple task
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(default="")
    status = models.CharField(max_length=20,choices=TASK_TYPE,default="To Do")
    priority = models.CharField(max_length=10,choices=PRIORITY_LEVEL,default="High")
    due_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'tasks'

class TaskAssignmentMapping(BaseTimeStampModel):
    #a task assign to user and user can have multiple task
    user = models.ForeignKey(User,related_name='task_user', on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks,related_name='user_task', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(null=True)
    class Meta:
        db_table = 'task_assignment'


class Comments(BaseTimeStampModel):
    #a multiple user can comment on multiple task 
    task = models.ForeignKey(Tasks,related_name='task_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_comment', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = 'comments'