from flask_restful import Resource, reqparse
from swarm_intelligence_app.models.models import db
from swarm_intelligence_app.models.user import User as UserModel
from swarm_intelligence_app.common import errors
from swarm_intelligence_app.common.oauth import auth
from flask import g

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('firstname', required=True)
parser.add_argument('lastname', required=True)
parser.add_argument('email', required=True)


class UserList(Resource):
    @auth.login_required
    def post(self):
        user = UserModel.query.filter_by(googleid=g.data["sub"]).first()
        print(g.data)
        print(user)
        if user is not None:
            return {"Message":"User already exists"}
        else:
            db.session.add(UserModel(g.data["name"], g.data["family_name"], g.data["email"], g.data["sub"]))
            db.session.commit()
            return {'users': 'create'}

    @auth.login_required
    def get(self):
        users = UserModel.query.all()
        list = [i.serialize for i in users]
        print(g.data)
        return {'users': list}


class User(Resource):
    @auth.login_required
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if user == None:
            raise errors.EntityNotFoundError('User', user_id)
        return {'users': [user.serialize]}

    @auth.login_required
    def put(self, user_id):
        args = parser.parse_args()
        user = UserModel.query.get(user_id)
        if user == None:
            raise errors.EntityNotFoundError('User', user_id)
        user.firstname = args['firstname']
        user.lastname = args['lastname']
        user.email = args['email']
        db.session.commit()
        return {'users': 'update'}

    @auth.login_required
    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user == None:
            raise errors.EntityNotFoundError('User', user_id)
        db.session.delete(user)
        db.session.commit()
        return {'users': 'delete'}