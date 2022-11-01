from flask import Flask, request

from .. import db, api
from .models import Task
from .resources import resource_fields
from flask_restful import Resource, abort, marshal_with


def abort_if_task_doesnt_exist(id):
    if id not in Task.query.all():
        abort(404, message=f"Could not find task with that {id}")


class TaskList(Resource):
    """
    Shows a list of all tasks, and lets you POST to add new tasks
    """
    @marshal_with(resource_fields)
    def get(self):
        tasks = Task.query.order_by(Task.timestamp.desc()).all()
        return tasks, 201

    @marshal_with(resource_fields)
    def post(self):
        data = request.json
        task = Task(name=data['name'], description=data['description'])
        db.session.add(task)
        db.session.commit()
        tasks = Task.query.order_by(Task.timestamp.desc()).all()
        return tasks, 201


class TaskSingle(Resource):
    """
    Shows a single todo item and lets you delete a todo item
    """
    @marshal_with(resource_fields)
    def get(self, id):
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort_if_task_doesnt_exist(id)
        return task, 201

    @marshal_with(resource_fields)
    def put(self, id):
        abort_if_task_doesnt_exist(id)
        data = request.json
        task = Task.query.filter_by(id=id).first()
        task.name = data['name']
        task.description = data['description']
        db.session.commit()
        return task, 201

    @marshal_with(resource_fields)
    def delete(self, id):
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort_if_task_doesnt_exist(id)
        db.session.delete(task)
        db.session.commit()
        tasks = Task.query.order_by(Task.timestamp.desc()).all()
        return tasks, 204


api.add_resource(TaskList, '/')
api.add_resource(TaskSingle, '/task/<int:id>/')
