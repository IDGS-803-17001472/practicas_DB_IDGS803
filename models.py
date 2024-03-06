from flask_sqlalchemy import SQLAlchemy

import datetime

db=SQLAlchemy()

class Empleados(db.Model):
    _tablename_='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    telefono=db.Column(db.BigInteger)
    email=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    sueldo=db.Column(db.Double)
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)


class EncabezadoVenta(db.Model):
    _tablename_='EncabezadoVenta'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    detalleVenta = db.relationship("DetalleVenta", backref=db.backref("EncabezadoVenta", uselist=False))
    telefono=db.Column(db.BigInteger)
    fecha_compra=db.Column(db.DateTime,default=datetime.datetime.now)
    
class DetalleVenta(db.Model):
    _tablename_='DetalleVenta'
    id=db.Column(db.Integer,primary_key=True)
    id_encabezado = db.Column(db.Integer, db.ForeignKey("EncabezadoVenta.id"))
    pina=db.Column(db.Boolean)
    jamon=db.Column(db.Boolean)
    champinones=db.Column(db.Boolean)
    cantidad=db.Column(db.Integer)
    tamanio=db.Column(db.String(20))
    