from flaskext.mysql import MySQL
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

mysql = MySQL()

# MYSQL configurations:
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'swarm_intelligence_test'
app.config['MYSQL_DATABASE_host'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

def connect_db():
    """Connects to the specific database."""
    rv = mysql.connect(app.config['swarm_intelligence_test'])
    rv.row_factory = mysql.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.route('/')
def hello_world():
    return 'Hello World!4'

@app.route('/users')
def show_users():
    cursor.execute('select * from user')
    result = cursor.fetchall()
    #result = [{'id':1, 'user':"Felix"},{'id':2, 'user':"Tobias"}]
    return render_template('users.xml', data=result), 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run()
