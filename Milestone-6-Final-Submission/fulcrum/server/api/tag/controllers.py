from flask import Blueprint, jsonify, request, abort
from flask_login import current_user

from api import db, student_permission
from api.tag.models import Tag, TicketsTags
from api.ticket.models import Ticket


from api.tag.schemas import BulkTagSchema, TagSchema

tag_module = Blueprint('tag_api', __name__, url_prefix='/api/tags')

@tag_module.route('/create', methods=['POST'])
@student_permission.require()
def create():
    data = {k: v.strip() for k, v in request.get_json().items()}
    schema = BulkTagSchema()
    errors = schema.validate(data)
    # errors = False

    if errors:
        # Validation Error
        abort(422, str(errors))
    else:
        tags = data['tag_list'].split(",")
        tags = [x.strip(' ') for x in tags]

        existing = {}
        for tag in tags:
            t = Tag.query.filter_by(name=tag).first()
            if t:
                existing[t.name] = t.id
            else:
                t = Tag(name=tag, user_id=current_user.id)
                db.session.add(t)
                db.session.commit()
                existing[t.name] = t.id
        return jsonify(existing)

@tag_module.route('/list', methods=['GET'])
# @student_permission.require()
def fetch_all():
    tags = Tag.query.all()
    schema = TagSchema()
    return schema.dump(tags, many=True)


@tag_module.route('/list/my', methods=['GET'])
@student_permission.require()
def fetch_my():
    tags = Tag.query.filter_by(user_id=current_user.id).all()
    schema = TagSchema()
    return schema.dump(tags, many=True)

@tag_module.route('/list/tickets/<ticket_id>', methods=['GET'])
@student_permission.require()
def fetch_tags_for_ticket(ticket_id):
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    if ticket:
        tags = ticket.tags
        schema = TagSchema()
        return schema.dump(tags, many=True)
    else:
        abort(404, 'Ticket does not exist')