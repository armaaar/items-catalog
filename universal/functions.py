# Hashing
import hashlib
import hmac
# Salting
import string
import random
# Forms rendering
from flask import render_template
## for auth functions
from pages._auth import auth

def create_salt(length=32):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))

def hash_it(password, salt=None, salt_it=True):
    if salt_it and not salt:
        salt = create_salt()
    if salt_it:
        return hmac.new(str(salt), msg=str(password), digestmod=hashlib.sha256).hexdigest()
    else:
        return hashlib.sha256(str(password)).hexdigest()

def add_breaks(string):
    return str(string).replace('\n', '<br />')

login_required_dummy_view = auth.login_required(lambda: None)
def is_loggedin():
    try:
        # default implementation returns a string error
        return login_required_dummy_view() is None
    except HTTPException:
        # in case auth_error_callback raises a real error
        return False

def render_form(form, form_action, form_method="POST"):
    return render_template("includes/form.jinja", form=form, form_action=form_action, form_method=form_method)
