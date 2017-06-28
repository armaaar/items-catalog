from flask import Flask, send_from_directory, g, session
from flask_wtf.csrf import CSRFProtect
from universal import *
from pages import *
from datetime import timedelta

app = Flask(__name__)
# Enable CSRF protection globally
#csrf = CSRFProtect(app)

# Extend flask session time


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

# define custom statics


@app.route('/js/<path:filename>', endpoint='js')
def static_scripts(filename):
    return send_from_directory("static/scripts", filename)


@app.route('/css/<path:filename>', endpoint='css')
def static_styles(filename):
    return send_from_directory("static/styles", filename)


@app.route('/imgs/<path:filename>', endpoint='imgs')
def static_scripts(filename):
    return send_from_directory("static/images", filename)


# App routes
app.add_url_rule("/", "index", home.home)
# login / logout
app.add_url_rule("/login/", "login", login.login, methods=["POST"])
app.add_url_rule("/logout/", "logout", logout.logout)
# categories
app.add_url_rule("/categoty/<int:category_id>/", "category", category.handler)
# items
app.add_url_rule("/item/<int:item_id>/", "item", item.handler)
app.add_url_rule("/additem/", "add_item",
                 add_item.handler, methods=["GET", "POST"])
app.add_url_rule("/edititem/<int:item_id>/", "edit_item",
                 edit_item.handler, methods=["GET", "POST"])
app.add_url_rule("/deleteitem/<int:item_id>/", "delete_item",
                 delete_item.handler, methods=["GET", "POST"])
# API
app.add_url_rule("/api/v1/", "JSON", api.handler)

if __name__ == '__main__':
    app.secret_key = functions.create_salt()
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
