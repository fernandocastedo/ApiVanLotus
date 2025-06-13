from flask import Blueprint, request, jsonify
from app.models import Producto, db

producto_bp = Blueprint('producto', __name__, url_prefix='/productos')

@producto_bp.route('/', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos])

@producto_bp.route('/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    return jsonify(producto.to_dict())

@producto_bp.route('/', methods=['POST'])
def create_producto():
    data = request.json
    producto = Producto(
        nombre=data['nombre'],
        precio_compra=data['precio_compra'],
        precio_venta=data['precio_venta'],
        cantidad_disponible=data['cantidad_disponible'],
        tipo_id=data['tipo_id']
    )
    db.session.add(producto)
    db.session.commit()
    return jsonify(producto.to_dict()), 201

@producto_bp.route('/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    data = request.json
    producto.nombre = data.get('nombre', producto.nombre)
    producto.precio_compra = data.get('precio_compra', producto.precio_compra)
    producto.precio_venta = data.get('precio_venta', producto.precio_venta)
    producto.cantidad_disponible = data.get('cantidad_disponible', producto.cantidad_disponible)
    producto.tipo_id = data.get('tipo_id', producto.tipo_id)
    db.session.commit()
    return jsonify(producto.to_dict())

@producto_bp.route('/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    db.session.delete(producto)
    db.session.commit()
    return '', 204 