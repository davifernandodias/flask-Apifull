from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
    "name":"davi",
    "age":19,
    "logaduro": "travessa jose scarcela {247}"
    })
@app.route('/soma/<int:value_one>/<int:value_two>/')    
def soma(value_one,value_two):
    return jsonify({"soma":value_one+value_two})

if __name__ =="__main__":
    app.run(debug=True)