from api import db
from api.core.models import Base

class Tag(Base):
    __tablename__ = 'tags'
    
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(32), nullable=False, unique=True)
    tickets = db.relationship('Ticket', secondary='tickets_tags', backref=db.backref('tags'))

    # def bulk_create_for_user(user_id, tag_list):
    #     db.session.add()

class TicketsTags(Base):
    __tablename__ = 'tickets_tags'
    __table_args__ = (db.UniqueConstraint('ticket_id', 'tag_id'), )
    
    ticket_id = db.Column('ticket_id', db.Integer, db.ForeignKey('tickets.id'))
    tag_id = db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))