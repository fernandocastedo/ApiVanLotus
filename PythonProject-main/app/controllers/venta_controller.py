from flask import Blueprint, request, jsonify
from app.models import Venta, db

venta_bp = Blueprint('venta', __name__, url_prefix='/ventas')

@venta_bp.route('/', methods=['GET'])
def get_ventas():
    ventas = Venta.query.all()
    return jsonify([v.to_dict() for v in ventas])

@venta_bp.route('/<int:venta_id>', methods=['GET'])
def get_venta(venta_id):
    venta = Venta.query.get_or_404(venta_id)
    return jsonify(venta.to_dict())

@venta_bp.route('/', methods=['POST'])
def create_venta():
    data = request.json
    venta = Venta(
        usuario_id=data['usuario_id'],
        cliente_nombre=data.get('cliente_nombre'),
        cliente_telefono=data.get('cliente_telefono')
    )
    db.session.add(venta)
    db.session.commit()
    return jsonify(venta.to_dict()), 201

@venta_bp.route('/<int:venta_id>', methods=['PUT'])
def update_venta(venta_id):
    venta = Venta.query.get_or_404(venta_id)
    data = request.json
    venta.usuario_id = data.get('usuario_id', venta.usuario_id)
    venta.cliente_nombre = data.get('cliente_nombre', venta.cliente_nombre)
    venta.cliente_telefono = data.get('cliente_telefono', venta.cliente_telefono)
    db.session.commit()
    return jsonify(venta.to_dict())

@venta_bp.route('/<int:venta_id>', methods=['DELETE'])
def delete_venta(venta_id):
    venta = Venta.query.get_or_404(venta_id)
    db.session.delete(venta)
    db.session.commit()
    return '', 204 