import json
from flask import Flask, request
from flask_restful import Resource, Api

import habilidades
from habilidades import Habilidade, Retorna_habilidades
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
    'id':0,
    'nome':'Fernando',
    'habilidades':['python','flask']
    },
    {
    'id':1,
    'nome':'Rafael',
    'habilidades':['python','django']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        #return desenvolvedores[id]['habilidades'][id]
        #return desenvolvedores[id]
        try:
            #desenvolvedor = desenvolvedores[id]
            #return jsonify(desenvolvedor)
            print(desenvolvedores[0]['habilidades'])
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'statur':'Erro','mensagem':mensagem}
        return (response)

    def put(self, id):
        dados = json.loads(request.data)
        if dados['habilidades[0]'] not in habilidades.list_habilidades:
            return 'Habilidade não permitida!'
        else:

            desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status': 'sucesso', 'mensaem': 'Registro excluído.'})

class Lista_desenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):

        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao  # O parametro id do dicionario recebe o indice
        desenvolvedores.append(dados)
        # return jsonify({'status':'sucesso', 'mensagem':'registro inserido.'})
        return (desenvolvedores[posicao])

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_desenvolvedores, '/dev/')
api.add_resource(Habilidade, '/habilidades/<int:id>/')
api.add_resource(Retorna_habilidades, '/habilidades/')
if __name__ == '__main__':
    app.run(debug=True)
