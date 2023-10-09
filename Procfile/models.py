from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), nullable=False)
    numero_documento = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    telefonos = db.relationship('Telefono', backref='contacto', lazy=True)
    correos = db.relationship('Correo', backref='contacto', lazy=True)


class Telefono(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False)
    contacto_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)

class Correo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(100), nullable=False)
    contacto_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
