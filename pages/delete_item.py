
from _imports import *
from db import *


@universal.functions.item_owner
def handler(item_id):
    if request.method == "GET":
        return show_form(item_id=item_id)
    elif request.method == "POST":
        return delete_item(item_id=item_id)


@universal.functions.item_owner
def show_form(item_id):
    item = db_session.query(Item).filter_by(id=item_id).one()
    items = db_session.query(Item).filter(and_(
        Item.category_id == item.category_id, Item.id != item_id)).order_by('name').all()

    set_page_info(title="Delete '%s' Item" % (item.name,))
    return render_template("delete_item.jinja", items=items, item=item)


@universal.functions.item_owner
def delete_item(item_id):
    item = db_session.query(Item).filter_by(id=item_id).one()
    category_id = item.category_id

    db_session.delete(item)
    db_session.commit()

    return redirect(url_for("category", category_id=category_id))
