from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # cors = CORS(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:w1llres0lve@localhost/sooraj'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.init_app(app)

    from .views import main
    app.register_blueprint(main)
    
    return app
