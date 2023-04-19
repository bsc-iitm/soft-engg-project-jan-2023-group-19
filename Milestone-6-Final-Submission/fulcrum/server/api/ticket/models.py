from api import db
from api.core.models import Base

class Ticket(Base):
    __tablename__ = 'tickets'

    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    views = db.Column(db.Integer, nullable=False, default=1)
    faqed = db.Column(db.Boolean, nullable=False, default=False)
    status = db.Column(db.String(32), nullable=False, default="open")
    subject = db.Column(db.String(255), nullable=False)
    # tags = db.relationship('Tag', secondary='tickets_tags', backref=db.backref('tickets', lazy='dynamic'))
    responses = db.relationship('Response', backref=db.backref('ticket'))
    votes = db.relationship('Vote', backref=db.backref('ticket'))

class Response(Base):
    __tablename__ = 'responses'

    ticket_id = db.Column('ticket_id', db.Integer, db.ForeignKey('tickets.id'))
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.Text(), nullable=False)
