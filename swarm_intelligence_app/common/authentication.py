import requests
from swarm_intelligence_app.models.user import User as UserModel
from oauth2client import client, crypt
from swarm_intelligence_app.common.oauth import auth
from flask import g


@auth.verify_token
def verify_token(token):
    CLIENT_ID = "92860260003-c8pdh6l63it0g2n84g7ksf7knu1ttge6.apps.googleusercontent.com"
    try:
        idinfo = client.verify_id_token(token, CLIENT_ID)
        # If multiple clients access the backend server:
        #if idinfo['aud'] not in [ANDROID_CLIENT_ID, IOS_CLIENT_ID, WEB_CLIENT_ID]:
        #    raise crypt.AppIdentityError("Unrecognized client.")
        #if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        #    raise crypt.AppIdentityError("Wrong issuer.")
        #if idinfo['hd'] != APPS_DOMAIN_NAME:
        #    raise crypt.AppIdentityError("Wrong hosted domain.")
    except crypt.AppIdentityError:
    # Invalid token
    #    userid = idinfo['sub']
        return False
    print(token)
    tokenrequest = requests.get("https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=" + token)
    g.data = tokenrequest.json()
    #email = data["email"]
    #name = data["name"]
    #family_name = data["family_name"]
    return True


def authentication(token, google_id):
    if verify_token(token) is True:
        user = UserModel.query.filter_by(googleid=google_id)
        if user is None:
            print("User is not registered")
        else:
            print("User is registered")