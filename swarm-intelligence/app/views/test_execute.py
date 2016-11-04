from app.models import user
from flask import render_template
from app.views import view_path as user_path


@user_path.route('/execute/')
def execute():
    result = user.User.query.all()
    array = []
    for item in result:
       array.append([item.id, item.user])
       print(array)
    return render_template('users.xml', data=array), 200, {'Content-Type': 'application/xml'}
