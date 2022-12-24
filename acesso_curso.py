from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "https://cursos.uec.org.br"}})

@app.route('/', methods=['GET'])
def acesso_curso():
    # Lê o código enviado na solicitação
    pedido = request.args.get('acesso')

    # Abre o arquivo JSON com os pares de códigos e hashes
    with open('links.json', 'r') as f:
        data = json.load(f)

    for i in data:
        if i['pedido'] == pedido:
            retorno = app.response_class(
              response=json.dumps(i['hash']),
              status=200,
              mimetype='application/json'
            )
            return retorno

    retorno = app.response_class(
              response=None,
              status=200,
              mimetype='application/json'
            )
    return retorno

if __name__ == '__main__':
    app.run()
