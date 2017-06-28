from flask import Flask, send_from_directory, g
from flask_wtf.csrf import CSRFProtect
from universal import *
from pages import *

app = Flask(__name__)
# Enable CSRF protection globally
#csrf = CSRFProtect(app)

#define custom statics
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
app.add_url_rule("/login/", "login", login.login, methods=["POST"])
app.add_url_rule("/logout/", "logout", logout.logout)
app.add_url_rule("/additem/", "add_item", add_item.handler, methods=["GET", "POST"])

if __name__ == '__main__':
  app.secret_key = functions.create_salt()
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
