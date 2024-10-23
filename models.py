from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class Pet(db.Model):
    __tablename__ = "pets" 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default = DEFAULT_IMG)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.String(15), nullable=False, default = "Unadoptable") 
    #  I'm defaulting to false because I assume some animals need health screening and then will be changed availible once ready and approved



def connect_db(app): 
    db.app = app
    db.init_app(app)


    