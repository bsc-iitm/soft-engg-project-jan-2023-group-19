from api import db
from api.core.models import Base

class Vote(Base):
    __tablename__ = 'votes'
    __table_args__ = (db.UniqueConstraint('user_id', 'ticket_id'), )

    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    ticket_id = db.Column('ticket_id', db.Integer, db.ForeignKey('tickets.id'))
    upped = db.Column(db.Boolean(), nullable=False, default=True)
