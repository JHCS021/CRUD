
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos simulada en memoria
usuarios = []

@app.route('/')
def index():
    return redirect(url_for('listar_usuarios'))

@app.route('/usuarios')
def listar_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)


@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        edad = request.form['edad']
        usuarios.append({'nombre': nombre, 'correo': correo, 'edad': edad})
        return redirect(url_for('listar_usuarios'))
    return render_template('crear_usuario.html')


if __name__ == '__main__':
    app.run(debug=True)
