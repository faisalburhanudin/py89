from pos.models import db


class Products(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Integer, nullable=False)

    price = db.Column(db.Integer, nullable=False)

    stock = db.Column(db.Integer, nullable=False)
