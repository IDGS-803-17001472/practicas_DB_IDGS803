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