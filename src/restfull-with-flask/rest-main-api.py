from flask import Flask,request
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)

devolpers = [
    {'id':0
    ,'name':'davi',
    'hability':['Python','Django']
    },
    {'id':1
    ,
    'name':'Gabriel',
    'hability':['Python','Django']
    }
]

class Devolper(Resource):
    def get(self,id):
        try:
            response=devolpers[id]
        except IndexError:
            mensagem = f'Devolver of id {id} não existe'
            response = {'status':'erro','mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido. procuro adminstritador da api'
            response = {'status':'erro','mensagem': mensagem}
        return response
    def put(self,id):
        dados = json.loads(request.data)
        devolpers[id]=dados
        return dados
    def delete(self,id):
        devolpers.pop(id)
        return {'status': 'sucesso','mensagem': 'registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return devolpers

    def post(self):
        dados=json.loads(request.data)
        posicao = len(devolpers)
        dados['id']= posicao
        devolpers.append(dados)
        return devolpers[posicao]

api.add_resource(Devolper,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/')

if __name__ == '__main__':
    app.run(debug=True)
