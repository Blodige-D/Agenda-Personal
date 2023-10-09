from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Contact, Telefono, Correo  # Importa los modelos
from forms import ContactoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sED$GG^W&gscpSH&46PPKiAJbq62Kf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_agenda.db'
app.config['STATIC_FOLDER'] = 'static'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def listar_contactos():
    contactos = Contact.query.all()
    return render_template('listar_contactos.html', contactos=contactos)

@app.route("/registrar_contacto", methods=['GET', 'POST'])
def registrar_contacto():
    form = ContactoForm(request.form)
    if request.method == 'POST':
        print(request.form)
        if form.validate_on_submit():
            # Crear un nuevo contacto
            nuevo_contacto = Contact(
                nombre_completo=form.nombre_completo.data,
                numero_documento=form.numero_documento.data,
                direccion=form.direccion.data,
            )

            # Crear teléfonos para el contacto
            print(form.telefonos)
            telefonos = [Telefono(numero=telefono["numero"]) for telefono in form.telefonos.data]
            nuevo_contacto.telefonos = telefonos

            # Crear correos electrónicos para el contacto
            print(form.correos.data)
            correos = [Correo(direccion=correo["direccion"]) for correo in form.correos.data]
            nuevo_contacto.correos = correos

            # Agregar el nuevo contacto a la base de datos y guardar los cambios
            db.session.add(nuevo_contacto)
            db.session.commit()

            flash('El contacto se ha registrado con éxito', 'success')  # Mensaje de éxito
            return redirect(url_for('listar_contactos'))
        else:
            # Imprimir los errores de validación para depuración
            print(form.errors)
    return render_template('registrar_contacto.html', form=form)

@app.route("/editar_contacto/<int:id>", methods=['GET', 'POST'])
def editar_contacto(id):
    contacto = Contact.query.get_or_404(id)
    form = ContactoForm(obj=contacto)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Actualiza los datos del contacto según los cambios realizados en el formulario
        form.populate_obj(contacto)
        db.session.commit()
        flash('El contacto se ha actualizado con éxito', 'success')
        return redirect(url_for('listar_contactos'))
    else:
        # Imprimir los errores de validación para depuración
        print(form.errors)
    
    return render_template('editar_contacto.html', form=form, contacto=contacto)

@app.route('/eliminar_contacto/<int:id>', methods=['POST'])
def eliminar_contacto(id):
    contacto = Contact.query.get(id)
    
    # Eliminar todos los teléfonos asociados al contacto
    for telefono in contacto.telefonos:
        db.session.delete(telefono)
    
    # Luego eliminar los correos asociados al contacto
    for correo in contacto.correos:
        db.session.delete(correo)
    
    # Eliminar el contacto en sí
    db.session.delete(contacto)
    db.session.commit()
    
    flash('El contacto ha sido eliminado con éxito', 'success')
    
    return redirect(url_for('listar_contactos'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

