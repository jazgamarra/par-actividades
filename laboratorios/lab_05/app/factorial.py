from flask import Blueprint, request, render_template, session

factorial_bp = Blueprint('factorial_bp', __name__)

@factorial_bp.route('/factorial', methods=['GET', 'POST'])
def factorial():
    resultado = None
    mensaje = None

    if request.method == 'POST':
        try:
            numero = int(request.form.get('numero'))
            if numero < 1:
                mensaje = "Debe ser mayor que 0"
            else:
                resultado = 1
                for i in range(2, numero + 1):
                    resultado *= i
        except:
            mensaje = "Entrada inválida"

    session['visitas'] = session.get('visitas', 0) + 1

    return render_template('factorial.html',
                           resultado=resultado,
                           mensaje=mensaje,
                           visitas=session['visitas'])
