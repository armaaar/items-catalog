from _imports import *

class LoginForm(FlaskForm):
    username = TextField("Username",[validators.Required("Please enter your username.")])
    password = PasswordField("Password",[validators.Required("Please enter your password")])
    submit = SubmitField("Test")
