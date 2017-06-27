from _imports import *
from pages import meta
from db import *

def home():
    categories = db_session.query(Category).all()
    items = db_session.query(Item).order_by(Item.id.desc()).limit(10)
    return render_template("home.jinja",meta=meta, categories=categories, items=items)
