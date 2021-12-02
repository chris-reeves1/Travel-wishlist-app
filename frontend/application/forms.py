from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CountryForm(FlaskForm):
    country_name = StringField("Country Name", validators=[DataRequired()])
    submit = SubmitField("Add country")