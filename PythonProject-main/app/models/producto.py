from app import db

class Producto(db.Model):
    __tablename__ = 'productos'

    producto_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio_compra = db.Column(db.Numeric(10, 2), nullable=False)
    precio_venta = db.Column(db.Numeric(10, 2), nullable=False)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tiposproducto.tipo_id'), nullable=False)

    tipo = db.relationship('TipoProducto', back_populates='productos')
    ofertas = db.relationship('Oferta', back_populates='producto')
    detalles_venta = db.relationship('DetalleVenta', back_populates='producto')

    def __repr__(self):
        return f'<Producto {self.nombre}>'

    def to_dict(self):
        return {
            'producto_id': self.producto_id,
            'nombre': self.nombre,
            'precio_compra': float(self.precio_compra),
            'precio_venta': float(self.precio_venta),
            'cantidad_disponible': self.cantidad_disponible,
            'tipo_id': self.tipo_id
        } 