from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    Migrate(app, db)

    from app.routes.producto_routes import producto_bp
    from app.routes.factura_routes import factura_bp

    app.register_blueprint(producto_bp, url_prefix='/v1/productos')
    app.register_blueprint(factura_bp, url_prefix='/v1/facturas')

    return app
