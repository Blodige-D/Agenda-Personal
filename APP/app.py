from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Contact, Telefono, Correo  # Importa los modelos

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_agenda.db'
db.init_app(app)

@app.route("/")
def index():
    # Lógica para mostrar la lista de contactos
    return "Lista de contactos"

@app.route("/contacto/<int:id>")
def mostrar_contacto(id):
    # Lógica para mostrar un contacto específico
    return f"Información del contacto {id}"

@app.route('/contactos')
def listar_contactos():
    contactos = Contact.query.all()
    return render_template('listar_contactos.html', contactos=contactos)

if __name__ == "__main__":
    app.run(debug=True)

