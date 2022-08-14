from flask_restful import fields


task_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'timestamp':  fields.DateTime(dt_format='rfc822')
}
