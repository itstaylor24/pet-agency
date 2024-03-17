from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
# connects database to SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"
# generates generic image for animals


def connect_db(app):
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

    # connects database to app

  

class Pet(db.Model):
    # creates class 
    __tablename__ = "pets"
    # name of table typically plural

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    species = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False)
    age = db.Column(db.Integer)
    imageurl = db.Column(db.Text)

    def imageurl(self):
        """Return image for pet -- bespoke or generic."""

        return self.imageurl or GENERIC_IMAGE
        # not sure why this function is needed--can we just put optional in model?
