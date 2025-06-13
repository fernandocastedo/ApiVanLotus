from flask import Blueprint, request, jsonify
from app.models import DetalleVenta, db

detalleventa_bp = Blueprint('detalleventa', __name__, url_prefix='/detalleventas')

@detalleventa_bp.route('/', methods=['GET'])
def get_detalleventas():
    detalles = DetalleVenta.query.all()
    return jsonify([d.to_dict() for d in detalles])

@detalleventa_bp.route('/<int:detalle_id>', methods=['GET'])
def get_detalleventa(detalle_id):
    detalle = DetalleVenta.query.get_or_404(detalle_id)
    return jsonify(detalle.to_dict())

@detalleventa_bp.route('/', methods=['POST'])
def create_detalleventa():
    data = request.json
    detalle = DetalleVenta(
        venta_id=data['venta_id'],
        producto_id=data['producto_id'],
        cantidad=data['cantidad'],
        precio_unitario=data['precio_unitario'],
        oferta_id=data.get('oferta_id'),
        subtotal=data.get('subtotal')
    )
    db.session.add(detalle)
    db.session.commit()
    return jsonify(detalle.to_dict()), 201

@detalleventa_bp.route('/<int:detalle_id>', methods=['PUT'])
def update_detalleventa(detalle_id):
    detalle = DetalleVenta.query.get_or_404(detalle_id)
    data = request.json
    detalle.venta_id = data.get('venta_id', detalle.venta_id)
    detalle.producto_id = data.get('producto_id', detalle.producto_id)
    detalle.cantidad = data.get('cantidad', detalle.cantidad)
    detalle.precio_unitario = data.get('precio_unitario', detalle.precio_unitario)
    detalle.oferta_id = data.get('oferta_id', detalle.oferta_id)
    detalle.subtotal = data.get('subtotal', detalle.subtotal)
    db.session.commit()
    return jsonify(detalle.to_dict())

@detalleventa_bp.route('/<int:detalle_id>', methods=['DELETE'])
def delete_detalleventa(detalle_id):
    detalle = DetalleVenta.query.get_or_404(detalle_id)
    db.session.delete(detalle)
    db.session.commit()
    return '', 204 