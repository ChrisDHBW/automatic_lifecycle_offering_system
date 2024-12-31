from flask import Flask, jsonify
from flask_cors import CORS
from Utils import Logger
import CommunicationHandler, CommunicationQueue

logger : Logger.Logger
port : int = 10040
address : str = "127.0.0.1"
domainName : str = "communicationbroker.local"
handler : CommunicationHandler.CommunicationHandler
queue : CommunicationQueue.CommunicationQueue

def initialize():
    handler = CommunicationHandler.CommunicationHandler()
    queue = CommunicationQueue.CommunicationQueue()
    
def run(self):
    return

app = Flask("Communicationbroker")
CORS(app)
    
@app.route('/communicate/now', methods=['POST'])
def postOffering():
    data = handler.createNewOfferingForCustomer()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
@app.route('/communicate/later', methods=['POST'])
def postOffering():
    data = handler.createNewOfferingForCustomer()
    success = True
    if success:
        return jsonify(data), 200
        
    else:
        return jsonify({}), 200
    
if __name__ == '__main__':
    initialize()
    context = ('custom.crt', 'custom_cert.key')
    app.run(debug=False, ssl_context=context)