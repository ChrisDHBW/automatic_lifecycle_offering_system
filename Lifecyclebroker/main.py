from flask import Flask, jsonify
from flask_cors import CORS
from Utils import Logger
import LifecycleBroker

logger : Logger.Logger
port : int = 10040
address : str = "127.0.0.1"
domainName : str = "lifecyclebroker.local"
broker : LifecycleBroker.LifecycleBroker

def initialize():
    broker = LifecycleBroker.LifecycleBroker()
    
def run(self):
    return

app = Flask("Lifecyclebroker")
CORS(app)
    
@app.route('/lifecycle/<productid>', methods=['POST'])
def postLifecycle(productid):
    data = broker.createOfferings()
    success = True
    if success:
        return jsonify(data), 200
    else:
        return jsonify({}), 200
    
@app.route('/lifecycle/<productid>', methods=['GET'])
def getLifecycle(productid):
    data = {}
    success = True
    if success:
        return jsonify(data), 200
    else:
        return jsonify({}), 200
    
@app.route('/lifecycle', methods=['GET'])
def getLifecycle():
    data = broker
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
if __name__ == '__main__':
    initialize()
    context = ('custom.crt', 'custom_cert.key')
    app.run(debug=False, ssl_context=context)