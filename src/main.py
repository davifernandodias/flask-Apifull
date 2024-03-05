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

@app.route('/dev/<int:id>/',methods=['GET','PUT'])
def devolper(id):
    if request.method == 'GET':
        devolper=devolpers[id]
        print(devolper)
        return jsonify(devolper)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devolpers[id] == dados
        return jsonify(dados)



if __name__ == '__main__':
    app.run(debug=True)