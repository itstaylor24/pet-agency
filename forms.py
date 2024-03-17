from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField,  SelectField, TextAreaField
from wtforms.validators import InputRequired,  Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a new pet"""
    name = StringField(
        "Pet Name",
            validators=[InputRequired(message="Pet name can't be blank")])
    
    species = SelectField(
        "Species", 
        choices=[('porcupine', 'Porcupine'), ('dog', 'Dog'),  ('cat', 'Cat')])
    # for choices, the first element in the tuple is the variable used and the second element 
    # is what the user actually sees
    
    imageurl = StringField(
        "Image URL",
        validators=[ Optional(), URL(message="must enter a valid URL")])
    age = IntegerField(
        "Age",
        validators=[ Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    
    notes = TextAreaField(
        "Notes", validators=[Optional()])
    
    available = BooleanField("Available")

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    name = StringField(
        "Pet Name",
        validators=[InputRequired(message="Pet name can't be blank")])
    
    species = SelectField(
        "Species", 
        choices=[('porcupine', 'Porcupine'), ('dog', 'Dog'),  ('cat', 'Cat')])

    imageurl = StringField(
        "Image URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Notes",
        validators=[Optional()]
    )

    age = IntegerField(
        "Age",
        validators=[ Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])

    available = BooleanField("Available?")