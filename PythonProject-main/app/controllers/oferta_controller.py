from flask import Blueprint, request, jsonify
from app.models import Oferta, db

oferta_bp = Blueprint('oferta', __name__, url_prefix='/ofertas')

@oferta_bp.route('/', methods=['GET'])
def get_ofertas():
    ofertas = Oferta.query.all()
    return jsonify([o.to_dict() for o in ofertas])

@oferta_bp.route('/<int:oferta_id>', methods=['GET'])
def get_oferta(oferta_id):
    oferta = Oferta.query.get_or_404(oferta_id)
    return jsonify(oferta.to_dict())

@oferta_bp.route('/', methods=['POST'])
def create_oferta():
    data = request.json
    oferta = Oferta(
        producto_id=data['producto_id'],
        precio_oferta=data['precio_oferta'],
        inicio=data['inicio'],
        fin=data.get('fin'),
        descripcion=data.get('descripcion'),
        activo=data.get('activo', True)
    )
    db.session.add(oferta)
    db.session.commit()
    return jsonify(oferta.to_dict()), 201

@oferta_bp.route('/<int:oferta_id>', methods=['PUT'])
def update_oferta(oferta_id):
    oferta = Oferta.query.get_or_404(oferta_id)
    data = request.json
    oferta.producto_id = data.get('producto_id', oferta.producto_id)
    oferta.precio_oferta = data.get('precio_oferta', oferta.precio_oferta)
    oferta.inicio = data.get('inicio', oferta.inicio)
    oferta.fin = data.get('fin', oferta.fin)
    oferta.descripcion = data.get('descripcion', oferta.descripcion)
    oferta.activo = data.get('activo', oferta.activo)
    db.session.commit()
    return jsonify(oferta.to_dict())

@oferta_bp.route('/<int:oferta_id>', methods=['DELETE'])
def delete_oferta(oferta_id):
    oferta = Oferta.query.get_or_404(oferta_id)
    db.session.delete(oferta)
    db.session.commit()
    return '', 204 