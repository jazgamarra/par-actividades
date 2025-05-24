from flask import Blueprint, render_template, current_app
import os

galeria_bp = Blueprint('galeria_bp', __name__)

@galeria_bp.route('/galeria')
def galeria():
    path = os.path.join(current_app.static_folder)
    imagenes = os.listdir(path)
    return render_template('galeria.html', imagenes=imagenes)
