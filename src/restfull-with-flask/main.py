from flask import Flask
from flask_restful import Resource, Api

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
    def put(self):
        pass
    def delete(self):
        pass

api.add_resource(Devolper,'/dev/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
