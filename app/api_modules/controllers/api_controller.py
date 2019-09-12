from flask import Blueprint

api_controller = Blueprint('api_controller', __name__, url_prefix='/api')


@api_controller.route('/', methods=['GET'])
def teste():
    return 'Teste, Hello World'
