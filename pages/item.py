from _imports import *
from db import *

def handler(item_id):
    item = db_session.query(Item).filter_by(id=item_id).one()
    items = db_session.query(Item).filter(and_(Item.category_id == item.category_id, Item.id != item_id)).order_by('name').all()

    set_page_info()
    return render_template("item.jinja", item=item, items=items)
