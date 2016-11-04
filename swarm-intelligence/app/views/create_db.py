from app.views import view_path as user_path
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from app.models import user



@user_path.route('/createdb/')
def create_db():
    engine = create_engine('mysql+pymysql://root:@localhost:3306/mydatabase')
    if not database_exists(engine.url):
        create_database(engine.url)
        user.db.create_all()
        user.db.session.commit()
    return "Engine has been created"
