from swarm_intelligence_app.models.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), unique=True)
    lastname = db.Column(db.String(45), unique=True)
    email = db.Column(db.String(100), unique=True)
    googleid = db.Column(db.String(100), unique=True)

    def __init__(self, firstname, lastname, email, googleid):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.googleid = googleid

    def __repr__(self):
        return '<User %r>' % self.email

    @property
    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'googleid': self.googleid
        }