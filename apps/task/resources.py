from flask_restful import fields


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'timestamp':  fields.DateTime(dt_format='rfc822')
}
