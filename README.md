# Introduction
The system allows users to manage their tasks by performing CRUD (Create, Read, Update, Delete)
operations. 
Features:
- it handle creation and assignment of task to user with the due date.
- task is created under a project


# Task Management API

This project is a Django-based API for managing tasks. The API provides functionalities for creating, updating, retrieving, and deleting tasks, as well as custom actions such as retrieving overdue tasks.

## Table of Contents

- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Overdue Tasks](#overdue-tasks)
- [License](#license)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rr4323/TMS_v2.git
cd TMS_v2
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv tms
source tms/bin/activate  
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run the migrations to set up the database schema.

```bash
cd src/TMS
python manage.py migrate
```

### 5. Create a Superuser (Optional)

To access the Django admin panel, you need to create a superuser.

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`


## API Endpoints

Here are the primary API endpoints available:

- **`GET /api/tasks/`**: Retrieve a list of all tasks.
- **`POST /api/tasks/`**: Create a new task.
- **`GET /api/tasks/{id}/`**: Retrieve a specific task by ID.
- **`PUT /api/tasks/{id}/`**: Update a specific task by ID.
- **`DELETE /api/tasks/{id}/`**: Delete a specific task by ID.
### Task Assignment and Status

- **`POST /api/v1/tasks/{id}/assign/`**: Assign a task to a user.
- **`POST /api/v1/tasks/{id}/unassign/`**: Unassign a task from a user.
- **`PUT /api/v1/tasks/{id}/complete/`**: Mark a task as complete.

### Comments on Tasks

- **`GET /api/v1/tasks/{id}/comments/`**: Retrieve all comments on a specific task.
- **`POST /api/v1/tasks/{id}/comments/`**: Add a comment to a specific task.
- **`DELETE /api/v1/tasks/{task_id}/comments/{comment_id}/`**: Delete a specific comment from a task.
### Project Management

- **`GET /api/v1/projects/`**: Retrieve a list of projects.
- **`GET /api/v1/projects/{id}/`**: Retrieve details of a specific project by its ID.
- **`POST /api/v1/projects/`**: Create a new project.
- **`PUT /api/v1/projects/{id}/`**: Update an existing project.
- **`DELETE /api/v1/projects/{id}/`**: Delete a specific project.
- **`GET /projects/{id}/progress/`**:Retrieve the progress of a
specific project.

## Overdue Tasks

The API provides a custom action to retrieve overdue tasks. A task is considered overdue if its due date is in the past and its status is not completed.

### Endpoint

- **`GET /api/tasks/overdue/`**: Retrieve a list of all overdue tasks.

### web browsable api
- **`http://localhost:8000/api/schema/swagger-ui/`**: web browsable api documentation


