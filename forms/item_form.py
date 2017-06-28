from _imports import *


class ItemForm(FlaskForm):
    name = TextField(
        "Title", [validators.Required("Please enter item title.")])
    description = TextAreaField("Description")
    category_id = SelectField("Category", coerce=int)
    submit = SubmitField("Submit")
