from app import db

class TipoProducto(db.Model):
    __tablename__ = 'tiposproducto'

    tipo_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    productos = db.relationship('Producto', back_populates='tipo')

    def __repr__(self):
        return f'<TipoProducto {self.nombre}>'

    def to_dict(self):
        return {
            'tipo_id': self.tipo_id,
            'nombre': self.nombre
        } 