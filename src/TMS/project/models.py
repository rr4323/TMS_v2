from django.db import models

# Create your models here.
# Project Model:
# ■ Project Model: A model to represent a project which can have multiple
# tasks.
# ■ Fields:
# ■ name: The name of the project.
# ■ description: A brief description of the project.
# ■ start_date: The start date of the project.
# ■ end_date: The expected completion date of the project.
# ■ created_at: The timestamp when the project was created.
# ■ updated_at: The timestamp when the project was last updated
class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='projects'

