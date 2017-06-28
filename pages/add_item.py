from _imports import *
from db import *
from forms import ItemForm

@universal.functions.require_login
def handler():
    form = ItemForm()
    form.category_id.choices = [(c.id, c.name) for c in db_session.query(Category).order_by('name')]

    if request.method == "GET":
        return show_form(form)
    elif request.method == "POST":
        return add_item(form)

@universal.functions.require_login
def show_form(form):
    set_page_info(title="Add Item")
    return render_template("add_item.jinja", form=form)

@universal.functions.require_login
def add_item(form):
    if form.validate() != False:
        item_name = request.form["name"]
        description = request.form["description"]
        category_id = request.form["category_id"]

        category = db_session.query(Category).filter_by(id=category_id).one()
        item = Item(name = item_name, description=description, category=category, user=g.user)

        db_session.add(item)
        db_session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("add_item.jinja", form=form)
