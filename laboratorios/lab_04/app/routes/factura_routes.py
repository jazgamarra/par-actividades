from flask import Blueprint, request, jsonify
from app import db
from app.models.factura import Factura
from app.schemas.factura_schema import FacturaSchema

factura_bp = Blueprint('factura_bp', __name__)
factura_schema = FacturaSchema()
facturas_schema = FacturaSchema(many=True)

@factura_bp.route('', methods=['GET'])
def get_all_facturas():
    facturas = Factura.query.all()
    return jsonify(facturas_schema.dump(facturas))

@factura_bp.route('/<int:id>', methods=['GET'])
def get_factura_by_id(id):
    factura = Factura.query.get_or_404(id)
    return jsonify(factura_schema.dump(factura))

@factura_bp.route('', methods=['POST'])
def create_factura():
    data = factura_schema.load(request.json, session=db.session)
    db.session.add(data)
    db.session.commit()
    return jsonify(factura_schema.dump(data)), 201

@factura_bp.route('/<int:id>', methods=['PUT'])
def update_factura(id):
    factura = Factura.query.get_or_404(id)
    updated = factura_schema.load(request.json, instance=factura, session=db.session)
    db.session.commit()
    return jsonify(factura_schema.dump(updated))

@factura_bp.route('/<int:id>', methods=['DELETE'])
def delete_factura(id):
    factura = Factura.query.get_or_404(id)
    db.session.delete(factura)
    db.session.commit()
    return '', 204
    