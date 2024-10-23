from flask import Flask, request, redirect, render_template, current_app, jsonify, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_ECHO'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

toolbar = DebugToolbarExtension(app)


# admin stuff
@app.route('/')
def home():
        # Home Page
        pets = Pet.query.order_by(Pet.name.desc()).all()
        
        return render_template("homepage.html", pets=pets)


@app.errorhandler(404)
def error(e): 
        return render_template('error.html'), 404


# adding pets

@app.route('/add',  methods=["GET", "POST"])
def add_pet():
        # add user post request
        form = PetForm()
        if form.validate_on_submit():
            # data = {key: value for key, value in form.data.items() if key != 'csrf_token'}
            # new_pet = Pet(**data)
            new_pet = Pet(
                name=form.name.data,
                species=form.species.data,
                photo_url=form.photo_url.data or None,
                age=form.age.data,
                notes=form.notes.data or None,
                available=form.available.data)

            db.session.add(new_pet)
            db.session.commit()
            return redirect("/")
        else:
            return render_template("new.html", form=form)


# specific user and capabilities
@app.route('/api/pets/<int:pet_id>', methods = ["GET"])
def pet_inspect(pet_id):
        # inspect user from directory - more info page
        pet = Pet.query.get_or_404(pet_id)
        info = {"name": pet.name, "age": pet.age}
        return jsonify(info)
# i dont really see this as helpful as the little show.html that i can control more 

@app.route('/<int:pet_id>')
def pet_show(pet_id):
       pet= Pet.query.get_or_404(pet_id)
       return render_template("show.html", pet=pet)

# edit

@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
       pet = Pet.query.get_or_404(pet_id)
       form = EditPetForm(obj=pet)
       if form.validate_on_submit():
              pet.notes = form.notes.data or None
              pet.available  = form.available.data
              pet.photo_url = form.photo_url.data

              db.session.commit()
              return redirect(url_for('home'))
       else:
              return render_template("edit.html", form=form, pet=pet)

@app.route('/<int:pet_id>/delete', methods=["POST"])
def delete_pet(pet_id):
        # delete user post request
        pet = Pet.query.get_or_404(pet_id)
        
        db.session.delete(pet)
        db.session.commit()
        return redirect("/")












# @app.route('/add', methods=["GET", "POST"])
# def add_pet():
#         # add user post request
#         new_pet = Pet(
#                 name = request.form['name'], 
#                 species = request.form['species'], 
#                 photo_url = request.form['photo_url'] or None,
#                 age = request.form['age'], 
#                 notes = request.form['notes'] or None, 
#                 available  = request.form['available'])
        
#         db.session.add(new_pet)
#         db.session.commit()
#         return redirect("/")


# @app.route('/<int:pet_id>/edit')
# def edit_pet_inspect(pet_id):
#         # edits inspected user from directory - more info page (form)
#         pet = Pet.query.get_or_404(pet_id)
#         return render_template("edit.html", pet=pet)

# @app.route('/<int:pet_id>/edit', methods=["POST"])
# def update_pet(pet_id):
#         # add user post request
#         pet = Pet.query.get_or_404(pet_id) 
#         pet.photo_url = request.form['photo_url'] or None
#         pet.notes = request.form['notes'] or None
#         pet.available  = request.form["available"]
        
#         db.session.add(pet)
#         db.session.commit()
#         return redirect(f"/{pet_id}")