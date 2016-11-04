from app.views import user_path
@user_path.route('/index/')
def hello_world():
    string = "Hello World!"
    return string
