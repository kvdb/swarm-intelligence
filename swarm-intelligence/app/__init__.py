from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/mydatabase'
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return "Diese Seite gibbet nich!"


from app.views import index, create_db, fill_db, test_execute
app.register_blueprint(index.user_path)
app.register_blueprint(create_db.user_path)
app.register_blueprint(fill_db.user_path)
app.register_blueprint(test_execute.user_path)
