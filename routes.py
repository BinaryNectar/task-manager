"""
routes.py

Defines RESTful API endpoints for managing tasks using Flask Blueprint.
Each route delegates to TaskService for business logic and handles HTTP errors.
"""

from flask import Blueprint, jsonify, request, abort
from database import init_db
from services import TaskService, TaskNotFoundError
from datetime import datetime

# Initialize database tables (creates tasks table if not exists)
init_db()

# Create a Flask Blueprint for routes to keep app modular
bp = Blueprint("routes", __name__)

# Instantiate the service layer for task operations
service = TaskService()

# Helper function for formatting date value
def format_date(input_string):
    if input_string:
        try:
            input_string = datetime.strptime(input_string, "%Y-%m-%d").date()
        except ValueError:
            abort(400, "Invalid date format for deadline; expected YYYY-MM-DD")
    else:
        input_string = None
    
    return input_string

@bp.route("/tasks", methods=["GET"])
def list_tasks():
    """
    GET /tasks

    Retrieve all tasks from the database.

    Returns:
        A JSON list of task dictionaries.
    """
    tasks = service.get_all_tasks()
    # Convert each Task model instance to a dict for JSON response
    return jsonify([t.to_dict() for t in tasks])

@bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """
    GET /tasks/<task_id>

    Retrieve a single task by its ID.

    Args:
        task_id (int): The ID of the task to fetch.

    Returns:
        A JSON object of the task.

    Raises:
        404 Not Found: If the task does not exist.
    """
    try:
        task = service.get_task(task_id)
    except TaskNotFoundError:
        # Abort with 404 if service indicates missing task
        abort(404)
    return jsonify(task.to_dict())

@bp.route("/tasks", methods=["POST"])
def create_task():
    """
    POST /tasks

    Create a new task with a title and optional completed status.

    Expects JSON body:
        {
            "title": str,            # required
            "dealine": date,         # optional
            "completed": bool        # optional, defaults to False
        }

    Returns:
        JSON of the created task and HTTP 201 status code.

    Raises:
        400 Bad Request: If 'title' field is missing in request JSON.
    """
    data = request.get_json()
    if not data or "title" not in data:
        # Missing required field 'title'
        abort(400, "Missing field: title")

    deadline = format_date(data.get("deadline", None))

    task = service.create_task(
        title=data["title"],
        deadline=deadline,
        completed=data.get("completed", False),
    )

    return jsonify(task.to_dict()), 201

@bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """
    PUT /tasks/<task_id>

    Update fields on an existing task.

    Args:
        task_id (int): The ID of the task to update.

    Expects JSON body with one or both:
        {
            "title": str,            # optional
            "deadline": date,        # optional
            "completed": bool        # optional
        }

    Returns:
        JSON of the updated task.

    Raises:
        404 Not Found: If the task does not exist.
    """
    data = request.get_json()

    deadline = format_date(data.get("deadline", None))

    try:
        task = service.update_task(
            task_id,
            title=data.get("title"),
            deadline=deadline,
            completed=data.get("completed"),
        )
    except TaskNotFoundError:
        abort(404)

    return jsonify(task.to_dict())

@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    DELETE /tasks/<task_id>

    Remove a task from the database by ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        Empty body with HTTP 204 status code on success.

    Raises:
        404 Not Found: If the task does not exist.
    """
    try:
        service.delete_task(task_id)
    except TaskNotFoundError:
        abort(404)

    # No content in response body
    return "", 204
