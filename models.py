from . import db

class employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key = True)
    name = db. Column(db.String(30))
    salary = db.Column(db.BigInteger)
