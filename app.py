from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets_agency"
app.config['SQLALCHEMY_ECHO'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)
app_context = app.app_context()
app_context.push()

db.create_all()

@app.route("/")
def list_pets():
    """Shows a list of all pets"""
   all_pets =  Pets.query.all()
   return render_template("homepage.html")

@app.route("/add",  methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data 
        photo_url= form.photo_url.data 
        notes = form.notes.data 
        age = form.age.data
        flash(f"Added new pet: name is {name}, age is ${age}")
        return redirect('/') 
    else:
        return render_template("add_pet.html")

@app.route("/<pet_id>",  methods=["GET", "POST"])
def display_edit_form(pet_id):
    """Displays info on a Pet and a form to edit pet info"""
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.image_url = form.image_url.data
        pet.notes = form.notes.data
        pet.notes = form.age.data
        db.session.commit()
        return redirect('/{pet.id}')
    else: return render_template('edit_pet.html')

