from flask import Flask
from app.views import main_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'PAR2025' # ya se que es una practica criminal

    app.register_blueprint(main_bp)

    return app