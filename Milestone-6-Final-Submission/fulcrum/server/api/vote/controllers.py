from flask import Blueprint, jsonify, request, abort
from flask_login import current_user

from api import db, student_permission
from api.vote.models import Vote

vote_module = Blueprint('vote', __name__, url_prefix='/api/tickets/<id>/vote')

@vote_module.route('/up', methods=['PATCH'])
@student_permission.require()
def up(id):
    vote = Vote.query.filter_by(ticket_id=id, user_id=current_user.id).first()
    if vote:
        # Already voted
        abort(422, str({'message': 'Voted already'}))
    else:
        vote = Vote(ticket_id=id, user_id=current_user.id)
        db.session.add(vote)
        db.session.commit()
        return jsonify({'status': 'OK', 'message': 'Voting successful'}), 201

@vote_module.route('/down', methods=['PATCH'])
@student_permission.require()
def down(id):
    vote = Vote.query.filter_by(ticket_id=id, user_id=current_user.id).first()
    if vote:
        # Already voted
        abort(422, str({'message': 'Voted already'}))
    else:
        vote = Vote(ticket_id=id, user_id=current_user.id, upped=False)
        db.session.add(vote)
        db.session.commit()
        return jsonify({'status': 'OK', 'message': 'Voting successful'}), 201

@vote_module.route('/cancel', methods=['DELETE'])
@student_permission.require()
def cancel(id):
    vote = Vote.query.filter_by(ticket_id=id, user_id=current_user.id).first()
    if vote:
        # Vote found
        db.session.delete(vote)
        db.session.commit()
        return jsonify({'status': 'OK', 'message': 'Vote cancelled'}), 201
    else:
        abort(422, str({'message': 'Vote not found'}))