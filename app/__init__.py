from flask import Flask
from dotenv import load_dotenv
import os

# Loading the enviroment variables from the .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['API_KEY'] = os.getenv("API_KEY")

    # Register blueprints or routes
    from .routes import main
    app.register_blueprint(main)

    return app