from flask import jsonify
from flask import Flask
app=Flask(__name__)


@app.route('/hello')
def hello_world():
    message = "hola mundo soy python con clould build hablando json"
    response = {
            "message" : message,
            "length" : len(message)
            }
    return jsonify(response)


@app.route('/bye')
def bye_world():
    return ("ADIOS TI@ FE@")
if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
