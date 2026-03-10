from app import db
from datetime import datetime

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id        = db.Column(db.Integer, primary_key=True)
    nombre    = db.Column(db.String(150), nullable=False)
    documento = db.Column(db.String(20), nullable=True)
    telefono  = db.Column(db.String(20), nullable=True)
    direccion = db.Column(db.String(200), nullable=True)

    ventas = db.relationship('Venta', backref='cliente', lazy=True)

    def __repr__(self):
        return f'<Cliente {self.nombre}>'


class Venta(db.Model):
    __tablename__ = 'ventas'

    id         = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    total      = db.Column(db.Numeric(14, 2), default=0)
    fecha      = db.Column(db.DateTime, default=datetime.now)

    detalles = db.relationship('DetalleVenta', backref='venta', lazy=True)

    def __repr__(self):
        return f'<Venta {self.id} - Total {self.total}>'


class DetalleVenta(db.Model):
    __tablename__ = 'detalle_ventas'

    id          = db.Column(db.Integer, primary_key=True)
    venta_id    = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad    = db.Column(db.Numeric(10, 2), nullable=False)
    precio_unit = db.Column(db.Numeric(12, 2), nullable=False)
    subtotal    = db.Column(db.Numeric(14, 2), nullable=False)

    producto = db.relationship('Producto', backref='detalles', lazy=True)

    def __repr__(self):
        return f'<DetalleVenta venta={self.venta_id} producto={self.producto_id}>'