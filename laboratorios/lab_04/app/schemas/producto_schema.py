from app.models.producto import Producto
from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        load_instance = True
