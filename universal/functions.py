# Hashing
import hashlib
import hmac
# Salting
import string
import random
# Forms rendering
from flask import render_template, session, make_response, g, redirect, url_for, flash
from db import *
import json


def create_salt(length=32):
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(length))


def hash_it(password, salt=None, salt_it=True):
    if salt_it and not salt:
        salt = create_salt()
    if salt_it:
        return hmac.new(str(salt), msg=str(password), digestmod=hashlib.sha256).hexdigest()
    else:
        return hashlib.sha256(str(password)).hexdigest()


def add_breaks(string):
    return str(string).replace('\n', '<br />')


def render_form(form, form_action, form_method="POST", **kwargs):
    return render_template("includes/form.jinja", form=form,
                           form_action=form_action, form_method=form_method, kwargs=kwargs)


def is_loggedin():
    user_id = session.get('user_id')
    if user_id is not None:
        user = db_session.query(User).filter_by(id=user_id).one()
        if user is None:
            return False
    else:
        return False
    g.user = user
    return True


def require_login(func):
    def func_wrapper(*args, **kwargs):
        if not is_loggedin():
            flash("You need to be loggedin to access that page.")
            return redirect(url_for("index"))
        return func(*args, **kwargs)
    return func_wrapper


def user_own_item(item_id):
    if not is_loggedin():
        return False
    user_id = session.get('user_id')
    item = db_session.query(Item).filter_by(id=item_id, user_id=user_id).one()
    if item is None:
        return False
    return True


def item_owner(func):
    def func_wrapper(*args, **kwargs):
        item_id = kwargs['item_id']
        if user_own_item(item_id) is not True:
            flash("You are not authorized to edit that item.")
            return redirect(url_for("item", item_id=item_id))
        return func(*args, **kwargs)
    return func_wrapper
