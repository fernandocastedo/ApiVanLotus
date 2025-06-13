from flask import Blueprint, request, jsonify
from app.models import TipoProducto, db

tipoproducto_bp = Blueprint('tipoproducto', __name__, url_prefix='/tiposproducto')

@tipoproducto_bp.route('/', methods=['GET'])
def get_tiposproducto():
    tipos = TipoProducto.query.all()
    return jsonify([t.to_dict() for t in tipos])

@tipoproducto_bp.route('/<int:tipo_id>', methods=['GET'])
def get_tipoproducto(tipo_id):
    tipo = TipoProducto.query.get_or_404(tipo_id)
    return jsonify(tipo.to_dict())

@tipoproducto_bp.route('/', methods=['POST'])
def create_tipoproducto():
    data = request.json
    tipo = TipoProducto(nombre=data['nombre'])
    db.session.add(tipo)
    db.session.commit()
    return jsonify(tipo.to_dict()), 201

@tipoproducto_bp.route('/<int:tipo_id>', methods=['PUT'])
def update_tipoproducto(tipo_id):
    tipo = TipoProducto.query.get_or_404(tipo_id)
    data = request.json
    tipo.nombre = data.get('nombre', tipo.nombre)
    db.session.commit()
    return jsonify(tipo.to_dict())

@tipoproducto_bp.route('/<int:tipo_id>', methods=['DELETE'])
def delete_tipoproducto(tipo_id):
    tipo = TipoProducto.query.get_or_404(tipo_id)
    db.session.delete(tipo)
    db.session.commit()
    return '', 204 