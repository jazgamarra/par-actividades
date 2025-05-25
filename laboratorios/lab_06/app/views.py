from flask import Blueprint, render_template, request, redirect, url_for, session

main_bp = Blueprint('main_bp', __name__)
usuarios = []  # lista temporal para almacenar usuarios

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/usuarios', methods=['POST'])
def guardar_usuario():
    ci = request.form.get('ci')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    telefono = request.form.get('telefono')

    usuario = {'ci': ci, 'nombre': nombre, 'apellido': apellido, 'telefono': telefono}
    usuarios.append(usuario)

    print(f"CI: {ci}, Nombre: {nombre}, Apellido: {apellido}, Teléfono: {telefono}")

    return redirect(url_for('main_bp.mostrar_usuarios'))

@main_bp.route('/usuarios', methods=['GET'])
def mostrar_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)
 