from flask import Blueprint, jsonify, request, abort
from database import init_db
from services import TaskService, TaskNotFoundError

bp = Blueprint("routes", __name__)
init_db()  # ensure tables exist

service = TaskService()

@bp.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = service.get_all_tasks()
    return jsonify([t.to_dict() for t in tasks])

@bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    try:
        task = service.get_task(task_id)
    except TaskNotFoundError:
        abort(404)
    return jsonify(task.to_dict())

@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        abort(400, "Missing field: title")
    task = service.create_task(
        title=data["title"],
        completed=data.get("completed", False),
    )
    return jsonify(task.to_dict()), 201

@bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    try:
        task = service.update_task(
            task_id,
            title=data.get("title"),
            completed=data.get("completed"),
        )
    except TaskNotFoundError:
        abort(404)
    return jsonify(task.to_dict())

@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        service.delete_task(task_id)
    except TaskNotFoundError:
        abort(404)
    return "", 204
