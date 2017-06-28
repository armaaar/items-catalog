from _imports import *
from db import *

def handler():
    categories = db_session.query(Category).order_by('name').all()
    items = db_session.query(Item).order_by(Item.id.desc()).all()
    lst= []
    for category in categories:
        items = db_session.query(Item).filter_by(category_id=category.id).order_by(Item.id).all()
        c = category.serialize
        c['items'] = [i.serialize for i in items]
        lst.append(c)
    return jsonify(category = lst)
