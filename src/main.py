from flask import Flask,jsonify

app = Flask(__name__)

devolpers = [
    {'name':'davi',
    'hability':['Python','Django']
    },
    {'name':'Gabriel',
    'hability':['Python','Django']
    }
]

@app.route('/dev/<int:id>/')
def devolper(id):
    devolper=devolpers[id]
    print(devolper)
    return jsonify(devolper)



if __name__ == '__main__':
    app.run(debug=True)