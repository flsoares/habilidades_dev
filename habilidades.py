import json
from flask_restful import request
from flask_restful import Resource

list_habilidades = [{'skill':'python','id':0},
                     {'skill':'Java','id':1},
                     {'skill':'Flask','id':2},
                     {'skill':'Php','id':3}]

#list_habilidades = ['python','Java','Flask','Php']

class Habilidade(Resource):
    def get(self, id):
        return list_habilidades[id]

    def put(self, id):

        dados = json.loads(request.data)
        list_habilidades[id] = dados
        return list_habilidades[id]

    def delete(self, id):
        list_habilidades.pop(id)
        response = {'mensagem':'Registro excluído.','status':'sucesso'}
        return response




class Retorna_habilidades(Resource):
    def get(self):
        return list_habilidades
    def post(self):
        dados = json.loads(request.data)
        posicao = len(list_habilidades)#verificar o tamanho da lista antes,para usar o indice
        list_habilidades.append(dados) # len retorna o tamanho començando conta do 1
        list_habilidades[posicao]['id']=posicao
        response ={'mensagem':'registro inserido','indice':posicao}
        return response