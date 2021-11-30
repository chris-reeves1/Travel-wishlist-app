from application import db

class Travel_wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination_name = db.Column(db.String(30), nullable=False)
    visited = db.Column(db.Boolean, nullable=False, default=False)