from _imports import *
from db import *
from forms import ItemForm

def item_owner(func):
    def func_wrapper(*args, **kwargs):
        item_id = kwargs['item_id']
        if universal.functions.user_own_item(item_id) is not True:
            flash("You are not authorized to edit that item.")
            return redirect(url_for("item", item_id=item_id))
        return func(*args, **kwargs)
    return func_wrapper

@universal.functions.item_owner
def handler(item_id):
    form = ItemForm()
    form.category_id.choices = [(c.id, c.name) for c in db_session.query(Category).order_by('name')]

    if request.method == "GET":
        return show_form(form, item_id=item_id)
    elif request.method == "POST":
        return edit_item(form, item_id=item_id)

@universal.functions.item_owner
def show_form(form, item_id):
    item = db_session.query(Item).filter_by(id=item_id).one()

    form.name.data = item.name
    form.description.data = item.description
    form.category_id.data = item.category_id

    set_page_info(title="Edit '%s' Item" % (item.name,))
    return render_template("edit_item.jinja", form=form, item_id=item_id)

@universal.functions.item_owner
def edit_item(form, item_id):
    if form.validate() != False:
        item_name = request.form["name"]
        description = request.form["description"]
        category_id = request.form["category_id"]

        item = db_session.query(Item).filter_by(id=item_id).one()
        category = db_session.query(Category).filter_by(id=category_id).one()

        item.name = item_name
        item.description = description
        item.category = category

        db_session.commit()
        return redirect(url_for("item", item_id=item_id))
    else:
        return render_template("edit_item.jinja", form=form)
