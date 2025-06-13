from flask import Blueprint, request, jsonify
from app.models import Usuario, db

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_bp.route('/', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])

@usuario_bp.route('/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    return jsonify(usuario.to_dict())

@usuario_bp.route('/', methods=['POST'])
def create_usuario():
    data = request.json
    usuario = Usuario(
        nombre_usuario=data['nombre_usuario'],
        contrasena_hash=data['contrasena_hash']
    )
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict()), 201

@usuario_bp.route('/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    data = request.json
    usuario.nombre_usuario = data.get('nombre_usuario', usuario.nombre_usuario)
    usuario.contrasena_hash = data.get('contrasena_hash', usuario.contrasena_hash)
    db.session.commit()
    return jsonify(usuario.to_dict())

@usuario_bp.route('/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    db.session.delete(usuario)
    db.session.commit()
    return '', 204 