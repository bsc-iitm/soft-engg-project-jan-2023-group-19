from api import mm
from marshmallow import Schema, fields
from marshmallow.validate import Length

class BulkTagSchema(Schema):
    tag_list = fields.Str(required=True, validate=Length(min=3, max=255))

class TagSchema(mm.Schema):
    class Meta:
        fields = ('id', 'name', 'user_id')