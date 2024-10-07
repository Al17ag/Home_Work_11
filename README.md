Creating an API for task management
Goal: Learn to work with the Django REST Framework to create, retrieve, and aggregate data using task models.

Task 1:
-------
Endpoint for creating a task
Create an endpoint to create a new task. The task must be created with the title, description, status, and deadline fields.

Steps to follow:

Define a serializer for the Task model.

Create a view to create a task.

Create a route to access the view.

Task 2: 
-------
Endpoint for getting a list of tasks with filters and pagination
Create an endpoint to receive a list of tasks filtered by status and deadline. Implement pagination of results.

Steps to follow:

Create a view to get a list of tasks with filters and pagination.

Create a route to access the view.

Task 3:
-------
Aggregating endpoint for task statistics
Create an endpoint to get task statistics, such as the total number of tasks, the number of tasks per status, and the number of overdue tasks.

Steps to follow:
Define a view to aggregate task data.

Create a route to access the view.

Format your answer as follows:

Endpoint code: Paste all the view and route code.

Testing screenshots: Attach screenshots of the console or Postman confirming the successful execution of requests for each endpoint.
