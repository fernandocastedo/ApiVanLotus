from app import db

class Oferta(db.Model):
    __tablename__ = 'ofertas'

    oferta_id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.producto_id'), nullable=False)
    precio_oferta = db.Column(db.Numeric(10, 2), nullable=False)
    inicio = db.Column(db.DateTime, nullable=False)
    fin = db.Column(db.DateTime, nullable=True)
    descripcion = db.Column(db.String(255))
    activo = db.Column(db.Boolean, nullable=False, default=True)

    producto = db.relationship('Producto', back_populates='ofertas')
    detalles_venta = db.relationship('DetalleVenta', back_populates='oferta')

    def __repr__(self):
        return f'<Oferta {self.oferta_id} - Producto {self.producto_id}>'

    def to_dict(self):
        return {
            'oferta_id': self.oferta_id,
            'producto_id': self.producto_id,
            'precio_oferta': float(self.precio_oferta),
            'inicio': self.inicio.isoformat() if self.inicio else None,
            'fin': self.fin.isoformat() if self.fin else None,
            'descripcion': self.descripcion,
            'activo': self.activo
        } 