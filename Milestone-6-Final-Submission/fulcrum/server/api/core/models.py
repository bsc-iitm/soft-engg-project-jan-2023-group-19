from api import db

class Base(db.Model):
    __abstract__ = True

    id         = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return ("<%s %d>" % (self.__class__.__name__, self.id))

