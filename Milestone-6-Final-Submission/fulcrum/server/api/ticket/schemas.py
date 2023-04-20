from api import mm
from marshmallow import Schema, fields
from marshmallow.validate import Length

class ResponseInputSchema(Schema):
    message = fields.Str(required=True, validate=Length(min=32))

class TicketInputSchema(ResponseInputSchema):
    subject = fields.Str(required=True, validate=Length(min=16))

class TicketSchema(mm.Schema):
    class Meta:
        fields = ('id', 'status', 'subject')