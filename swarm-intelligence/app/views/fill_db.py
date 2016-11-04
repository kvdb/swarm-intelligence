from app.models import user
from app.views import view_path as user_path


@user_path.route('/filldb/')
def fill_db():
    felix = user.User(1, 'Felix')
    tobias = user.User(2, 'Tobias')
    andreas = user.User(3, 'Andreas')

    user.db.session.add(felix)
    user.db.session.add(tobias)
    user.db.session.add(andreas)
    user.db.session.commit()
    return "Database has been filled"
