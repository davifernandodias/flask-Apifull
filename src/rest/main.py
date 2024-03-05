from flask import Flask,jsonify,request
import json
app = Flask(__name__)

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
# devolve um devolper pelo ID, too alter and delete a devolper
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

# Lista all devolper and add new devolper
@app.route('/dev/',methods=['POST','GET'])
def lista_devolper():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devolpers)
        dados['id'] = posicao
        devolpers.append(dados)
        return jsonify(devolpers[posicao])
    elif request.method == 'GET':
        return jsonify(devolpers)
        



if __name__ == '__main__':
    app.run(debug=True)