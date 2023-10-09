from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Email

class TelefonoForm(FlaskForm):
    numero = StringField('Número de Teléfono', validators=[DataRequired()])

class CorreoForm(FlaskForm):
    direccion = StringField('Dirección de Correo Electrónico', validators=[DataRequired(), Email()])

class ContactoForm(FlaskForm):
    nombre_completo = StringField('Nombre Completo', validators=[DataRequired()])
    numero_documento = StringField('Número de Documento')
    direccion = TextAreaField('Dirección')
    telefonos = FieldList(FormField(TelefonoForm), min_entries=1)
    correos = FieldList(FormField(CorreoForm), min_entries=1)
    submit = SubmitField('Registrar Contacto')
