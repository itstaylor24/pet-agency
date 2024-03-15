from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField,  SelectField
from wtforms.validators import InputRequired,  Optional, URL, NumberRange

class AddPetForm(FlaskForm)
name = StringField("Pet Name",  validators=[
                       InputRequired(message="Pet name can't be blank")])
species = SelectField("Species", choices=[
                          ('porcupine', 'dog',  'cat',)])
image_url = StringField('URL', validators=[ Optional(), URL(message="must enter a valid URL")])
age = IntegerField('Age', validators=[ Optional(), NumberRange(min=0, max=30),message="Age must be between 0 and 30"])
notes = StringField('Notes'), validators=[Optional()]