from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, URL, Optional, AnyOf, Length

class PetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    species = SelectField('Species', choices=[
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('horse', 'Horse'),
        ('rabbit', 'Rabbit'),
        ('porcupine', 'Porcupine')], validators=[DataRequired(message="Species must be one of: dog, cat, horse, rabbit, or porcupine")])
    
    photo_url = StringField('Photo URL', validators=[URL(require_tld=True, message='Invalid URL'), Optional()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = SelectField('Availability', choices=[('unadoptable', 'Unadoptable'), ('adoptable', 'Adoptable')], default='unadoptable')

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[URL(require_tld=True, message='Invalid URL'), Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = SelectField('Availability', choices=[('unadoptable', 'Unadoptable'), ('adoptable', 'Adoptable')], default='unadoptable')

    # submit = SubmitField('Add Pet')

