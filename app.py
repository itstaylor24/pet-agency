from flask import Flask, request, render_template,  redirect, flash, url_for, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets_agency"
app.config['SQLALCHEMY_ECHO'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

if __name__ == "__main__":
    app.run(debug=True)


connect_db(app)
app_context = app.app_context()
app_context.push()



@app.route("/")
def list_pets():
    """Shows a list of all pets"""
    all_pets =  Pet.query.all()
    return render_template("homepage.html", all_pets=all_pets)

@app.route("/add",  methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # above is a dict comprehension using unpacking, form.data.items is iterated over we use the 
        # k and v variables to construct a dict comprehension of the keys and values--only if the key is
        # not the csrf_token
        new_pet = Pet(**data)
        # above is an example of spreading a dictionary, sets and lists use only one asterisk
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        # still don't understand because this isn't the syntax for dictionaries???
       
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))
    # redirects back to the url for a specific view function

    else:
        # re-present form for editing
        return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>",  methods=["GET", "POST"])
def display_edit_form(pet_id):
    """Displays info on a Pet and a form to edit pet info"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.imageurl = form.imageurl.data
        pet.notes = form.notes.data
        pet.age = form.age.data
        db.session.commit()
        return redirect(url_for('list_pets'))
    else: return render_template('edit_pet.html', pet=pet, form=form)

