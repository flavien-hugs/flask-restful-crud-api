from flask_restful import fields


taskFieldsSerializers = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'timestamp': fields.DateTime
}
