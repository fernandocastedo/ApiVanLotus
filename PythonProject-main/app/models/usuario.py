from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), nullable=False)
    contrasena_hash = db.Column(db.String(255), nullable=False)

    ventas = db.relationship('Venta', back_populates='usuario')

    def __repr__(self):
        return f'<Usuario {self.nombre_usuario}>'

    def to_dict(self):
        return {
            'usuario_id': self.usuario_id,
            'nombre_usuario': self.nombre_usuario
        } 