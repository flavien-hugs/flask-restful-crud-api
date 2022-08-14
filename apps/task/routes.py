from flask import Flask, request

from .. import db, api
from .models import Task
from .serializers import taskFieldsSerializers
from flask_restful import Resource, marshal_with


class Items(Resource):
    @marshal_with(taskFieldsSerializers)
    def get(self):
        tasks = Task.query.order_by(Task.timestamp.desc()).all()
        return tasks

    @marshal_with(taskFieldsSerializers)
    def post(self):
        data = request.json
        task = Task(name=data['name'], description=data['description'])
        db.session.add(task)
        db.session.commit()
        tasks = Task.query.order_by(Task.timestamp.desc()).all()
        return tasks


class Item(Resource):
    @marshal_with(taskFieldsSerializers)
    def get(self, pk):
        task = Task.query.filter_by(id=pk).first()
        return task

    @marshal_with(taskFieldsSerializers)
    def put(self, pk):
        data = request.json
        task = Task.query.filter_by(id=pk).first()
        task.name = data['name']
        task.description = data['description']
        db.session.commit()
        return task

    @marshal_with(taskFieldsSerializers)
    def delete(self, pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        tasks = Task.query.order_by(Task.timestamp.desc()).all()
        return tasks


api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')
