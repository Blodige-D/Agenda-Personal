from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # Lógica para mostrar la lista de contactos
    return "Lista de contactos"

@app.route("/contacto/<int:id>")
def mostrar_contacto(id):
    # Lógica para mostrar un contacto específico
    return f"Información del contacto {id}"

if __name__ == "__main__":
    app.run(debug=True)

