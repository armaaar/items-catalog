from _imports import *
from pages import meta
from db import *
from flask import send_from_directory

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import requests
import json
import os

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

def login():
    #STEP 1 - Parse the auth code
    auth_code = request.data
    #STEP 2 - Exchange for a token
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(auth_code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    #STEP 3 - Find User or make a new one
    #Get user info
    h = httplib2.Http()
    userinfo_url =  "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt':'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    name = data['name']
    email = data['email']

    #see if user exists, if it doesn't make a new one
    user = db_session.query(User).filter_by(email=email).first()
    if not user:
        user = User(name = name, email = email)
        db_session.add(user)
        db_session.commit()

    #STEP 4 - Make session
    g.user = user
    session['user_id'] = user.id

    #STEP 5 - Send back token to the client
    return "ok"
