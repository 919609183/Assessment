from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    # ... other user fields if needed
