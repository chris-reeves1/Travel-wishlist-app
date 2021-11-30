from application import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(30), nullable=False)
    visited = db.Column(db.Boolean, nullable=False, default=False)
    recommend = db.Column(db.Boolean, nullable=False, default=False)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recommend = db.Column(db.Boolean, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)