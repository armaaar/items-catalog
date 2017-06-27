from flask import Flask, render_template, request, redirect,jsonify, url_for, flash, send_from_directory
from flask_wtf.csrf import CSRFProtect
from universal import *
from pages import *

app = Flask(__name__)
# Enable CSRF protection globally
csrf = CSRFProtect(app)

# App routes
app.add_url_rule("/", "index", home.main)

if __name__ == '__main__':
  app.secret_key = functions.create_salt()
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
