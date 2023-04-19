from api import mm
from marshmallow import Schema, fields
from marshmallow.validate import Length

class SigninInputSchema(Schema):
    email = fields.Str(required=True, validate=Length(min=8, max=255))
    password = fields.Str(required=True, validate=Length(min=6, max=255))

class SignupInputSchema(SigninInputSchema):
    first_name = fields.Str(required=True, validate=Length(min=2, max=64))
    last_name = fields.Str(required=True, validate=Length(min=2, max=64))
    roll_number = fields.Str(required=True, validate=Length(min=2, max=64))

class ProfileUpdateSchema(SigninInputSchema):
    first_name = fields.Str(required=True, validate=Length(min=2, max=64))
    last_name = fields.Str(required=True, validate=Length(min=2, max=64))

class UserSchema(mm.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'roll_number')