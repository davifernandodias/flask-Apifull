from flask import Flask,jsonify,request
import json
app = Flask(__name__)

devolpers = [
    {'name':'davi',
    'hability':['Python','Django']
    },
    {'name':'Gabriel',
    'hability':['Python','Django']
    }
]

@app.route('/dev/<int:id>/',methods=['GET','PUT','DELETE'])
def devolper(id):

    if request.method == 'GET':
        try:
            response=devolpers[id]
        except IndexError:
            mensagem = f'Devolver of id {id} não existe'
            response = {'status':'erro','mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido. procuro adminstritador da api'
            response = {'status':'erro','mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devolpers[id] == dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        devolpers.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro Excluido'})



if __name__ == '__main__':
    app.run(debug=True)