from app.views import view_path as user_path
@user_path.route('/index/')
def hello_world():
    string = "Hello World!"
    return string
