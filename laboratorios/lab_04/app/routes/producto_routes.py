from flask import Blueprint, request, jsonify
from app import db
from app.models.producto import Producto
from app.schemas.producto_schema import ProductoSchema

producto_bp = Blueprint('producto_bp', __name__)
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

@producto_bp.route('', methods=['GET'])
def get_all_productos():
    productos = Producto.query.all()
    return jsonify(productos_schema.dump(productos))

@producto_bp.route('/<int:id>', methods=['GET'])
def get_producto_by_id(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(producto_schema.dump(producto))

@producto_bp.route('', methods=['POST'])
def create_producto():
    data = producto_schema.load(request.json, session=db.session)
    db.session.add(data)
    db.session.commit()
    return jsonify(producto_schema.dump(data)), 201

@producto_bp.route('/<int:id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get_or_404(id)
    updated = producto_schema.load(request.json, instance=producto, session=db.session)
    db.session.commit()
    return jsonify(producto_schema.dump(updated))

@producto_bp.route('/<int:id>', methods=['DELETE'])
def delete_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return '', 204
