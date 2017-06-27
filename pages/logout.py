from _imports import *
from db import *
import httplib2
import json

def logout():

    if not session.get('access_token'):
    	flash("You already logged out.")
        print session.get('access_token')
    else :
        access_token = session['access_token']
        url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % session['access_token']
        h = httplib2.Http()
        result = h.request(url, 'GET')[0]

        if result['status'] == '200':
            del session['access_token']
            del session['gplus_id']
            del session['user_id']
            flash("You logged out successfully.")
        else:
        	flash("Failed to logout. Please try again.")

    return redirect(url_for("index"))
