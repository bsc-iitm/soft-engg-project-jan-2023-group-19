from api import db
from api.core.models import Base
from flask_security import UserMixin, RoleMixin

class RolesUsers(Base):
    __tablename__ = 'roles_users'

    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))

class Role(Base, RoleMixin):
    __tablename__ = 'roles'

    name = db.Column(db.String(32), unique=True)
    description = db.Column(db.Text)

class User(Base, UserMixin):
    __tablename__ = 'users'

    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    roll_number = db.Column(db.String(16), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(16))
    current_login_ip = db.Column(db.String(16))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    # tickets = db.relationship('Ticket', backref=db.backref('user', lazy='dynamic'))
    # tags = db.relationship('Tag', backref=db.backref('user', lazy='dynamic'))
    votes = db.relationship('Vote', backref=db.backref('user'))
