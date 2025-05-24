from flask import Blueprint, render_template
from datetime import datetime
import random

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html',
                           fecha=datetime.now(),
                           mayus="Texto a mayúsculas".upper(),
                           resultado=(5+2)/3.0,
                           aleatorio=random.randint(0, 100))
