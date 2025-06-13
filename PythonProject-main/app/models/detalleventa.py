from app import db

class DetalleVenta(db.Model):
    __tablename__ = 'detalleventas'

    detalle_id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.venta_id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.producto_id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    oferta_id = db.Column(db.Integer, db.ForeignKey('ofertas.oferta_id'))
    subtotal = db.Column(db.Numeric(10, 2))

    venta = db.relationship('Venta', back_populates='detalles')
    producto = db.relationship('Producto', back_populates='detalles_venta')
    oferta = db.relationship('Oferta', back_populates='detalles_venta')

    def __repr__(self):
        return f'<DetalleVenta {self.detalle_id}>'

    def to_dict(self):
        return {
            'detalle_id': self.detalle_id,
            'venta_id': self.venta_id,
            'producto_id': self.producto_id,
            'cantidad': self.cantidad,
            'precio_unitario': float(self.precio_unitario),
            'oferta_id': self.oferta_id,
            'subtotal': float(self.subtotal) if self.subtotal is not None else None
        } 