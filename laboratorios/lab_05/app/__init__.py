from flask import Flask
from app.routes import main_bp
from app.factorial import factorial_bp
from app.galeria import galeria_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecreto'

    app.register_blueprint(main_bp)
    app.register_blueprint(factorial_bp)
    app.register_blueprint(galeria_bp)

    return app
