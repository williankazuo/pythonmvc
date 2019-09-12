from flask import Flask

app = Flask(__name__)

# Modulos
from app.api_modules.controllers.api_controller import api_controller
app.register_blueprint(api_controller)