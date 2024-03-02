from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
    "name":"davi",
    "age":19,
    "logaduro": "travessa jose scarcela {247}"
    })

if __name__ =="__main__":
    app.run(debug=True)