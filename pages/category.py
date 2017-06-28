from _imports import *
from db import *


def handler(category_id):
    categories = db_session.query(Category).order_by('name').all()
    category = db_session.query(Category).filter_by(id=category_id).one()

    items = db_session.query(Item).filter_by(
        category_id=category_id).order_by(Item.id.desc()).all()
    items_count = len(items)

    set_page_info()
    return render_template("category.jinja", categories=categories,
                           category=category, items=items,
                           items_count=items_count)
