from flask_httpauth import HTTPBasicAuth
from flask import g
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(token):
    #Try to see if it's a token first
    user_id = User.verify_auth_token(token)
    if user_id:
        user = session.query(User).filter_by(id = user_id).one()
    else:
        return False
    g.user = user
    return True
