from _imports import *
from db import *


def home():
    categories = db_session.query(Category).order_by('name').all()
    items = db_session.query(Item).order_by(Item.id.desc()).limit(10)
    set_page_info()
    return render_template("home.jinja", categories=categories, items=items)
