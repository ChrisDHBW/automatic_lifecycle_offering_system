from flask import Flask, jsonify
from flask_cors import CORS
from Utils import Logger
import DataHandler

logger : Logger.Logger
port : int = 10010
address : str = "127.0.0.1"
domainName : str = "informationengine.local"
handler : DataHandler.DataHandler = DataHandler.DataHandler()

def initialize(self):
    pass
    
def run(self):
    return

app = Flask("Informationengine")
CORS(app)


@app.route('/customers', methods=['GET'])
def getCustomers():
    data =  handler.getCustomers()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify([]), 200
    
@app.route('/customer', methods=['POST'])
def postCustomer():
    data = handler.addCustomer()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/customer/<customerId>', methods=['GET'])
def getCustomer(customerId):
    data = handler.getCustomer(customerId)
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/customer/<customerId>', methods=['PATCH'])
def patchCustomer(customerId):
    data = handler.updateCustomer(customerId)
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200

@app.route('/customer/<customerId>', methods=['DELETE'])
def deleteCustomer(customerId):
    data = handler.deleteCustomer(customerId)
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200

@app.route('/products', methods=['GET'])
def getProducts():
    data = handler.getProducts()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/product', methods=['POST'])
def postProduct():
    data = handler.addProduct()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/product/<productId>', methods=['GET'])
def getProduct(productId):
    data = handler.getProduct(productId)
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/product/<productId>', methods=['PATCH'])
def patchProduct(productId):
    data = handler.updateProduct(productId)
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/system/statistics', methods=['GET'])
def getStatistics():
    data = handler.calculateStatistics()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/system/summary', methods=['GET'])
def getSummary():
    data = handler.summarizeSystem()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200

if __name__ == '__main__':
    initialize()
    context = ('custom.crt', 'custom_cert.key')
    app.run(debug=False, ssl_context=context)