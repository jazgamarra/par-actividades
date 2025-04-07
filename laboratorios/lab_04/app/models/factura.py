from app import db

class Factura(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
