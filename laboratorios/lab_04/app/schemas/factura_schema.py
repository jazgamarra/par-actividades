from app.models.factura import Factura
from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class FacturaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Factura
        load_instance = True
