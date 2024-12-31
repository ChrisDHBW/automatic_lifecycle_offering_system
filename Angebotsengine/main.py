from flask import Flask, jsonify
from flask_cors import CORS
from Utils import Logger
import OfferingCalculator

logger : Logger.Logger
port : int = 10020
address : str = "127.0.0.1"
domainName : str = "offeringengine.local"
calculator : OfferingCalculator.OfferingCalculator

def initialize():
    calculator = OfferingCalculator.OfferingCalculator()
    
def run(self):
    return

app = Flask("Offeringengine")
CORS(app)


@app.route('/offerings', methods=['GET'])
def getOfferings():
    data =  calculator.getOfferings()
    success = True
    if success:
        return jsonify(data), 200    
    else:
        return jsonify([]), 200
    
@app.route('/offering', methods=['POST'])
def postOffering():
    data = calculator.createNewOfferingForCustomer()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/offering/<offeringId>', methods=['GET'])
def getOffering(offeringId):
    data = calculator.getOffering(offeringId)
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/offering/<offeringId>', methods=['PATCH'])
def patchOffering(offeringId):
    newData = {}
    data = calculator.updateOffering(offeringId, newData)
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200

if __name__ == '__main__':
    initialize()
    context = ('custom.crt', 'custom_cert.key')
    app.run(debug=False, ssl_context=context)