from datetime import datetime
from app import db

class Venta(db.Model):
    __tablename__ = 'ventas'

    venta_id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), nullable=False)
    cliente_nombre = db.Column(db.String(100))
    cliente_telefono = db.Column(db.String(20))

    usuario = db.relationship('Usuario', back_populates='ventas')
    detalles = db.relationship('DetalleVenta', back_populates='venta')

    def __repr__(self):
        return f'<Venta {self.venta_id}>'

    def to_dict(self):
        return {
            'venta_id': self.venta_id,
            'fecha': self.fecha.isoformat() if self.fecha else None,
            'usuario_id': self.usuario_id,
            'cliente_nombre': self.cliente_nombre,
            'cliente_telefono': self.cliente_telefono
        } 