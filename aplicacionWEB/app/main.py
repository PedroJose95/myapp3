from flask import jsonify
from flask import request
from flask import Flask
from catalog import get_products
app=Flask(__name__)


@app.route('/product',methods=['GET', 'POST'])
def list_all_products():
    '''vemos todos los producto en el catalogo y tambien CRUD'''
    if request.method == 'GET':
        response = get_products()
        return jsonify(response)
    
    if request.method == 'POST':
        data = request.get_json()
        create_product(
                data['sku'],
                data['title'],
                data['long_descripcion'],
                data['price_euro'])
        return jsonify({"status": "ok"})
    
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
