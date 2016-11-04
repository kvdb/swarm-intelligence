from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.VARCHAR(50), unique=True)

    def __init__(self, id, user):
        self.id = id
        self.user = user

    def __repr__(self):
        return '<User %r>' % self.id

