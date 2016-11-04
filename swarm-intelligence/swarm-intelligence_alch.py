from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/swarm_intelligence_test'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.VARCHAR(50), unique=True)

    def __init__(self, id, user):
        self.id = id
        self.user = user

    def __repr__(self):
        return '<User %r>' % self.id

@app.route('/')
def hello_world():
   result = User.query.all()
   array = []

   for item in result:
       array.append([item.id, item.user])
       print(array)
   return render_template('users.xml', data=array), 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run()
