from flask import Flask, jsonify
from flask_cors import CORS
from Utils import Logger
from Accesspoints import Accesspoints
from Switches import Switches
from Gateways import Gateway
from Routers import Routers
from Firewalls import Firewalls

logger : Logger.Logger
port : int = 10030
address : str = "127.0.0.1"
domainName : str = "translationengine.local"
switches : Switches.Switches
aps : Accesspoints.Accesspoints
controllers : Gateway.Gateway
routers : Routers.Routers
firewalls : Firewalls.Firewalls

def initialize():
    pass
    
def run(self):
    return

app = Flask("TranslationEngine")
CORS(app)
    
@app.route('/translate/switch/<productid>', methods=['POST'])
def postLifecycle(productid):
    data = {}
    success = True
    if success:
        return jsonify(data), 200
    else:
        return jsonify({}), 200
    
@app.route('/translate/ap/<productid>', methods=['POST'])
def postLifecycle(productid):
    data = {}
    success = True
    if success:
        return jsonify(data), 200
    else:
        return jsonify({}), 200
    
@app.route('/translate/controller/<productid>', methods=['POST'])
def postLifecycle(productid):
    data = {}
    success = True
    if success:
        return jsonify(data), 200
    else:
        return jsonify({}), 200
    
@app.route('/translate/router/<productid>', methods=['POST'])
def postLifecycle(productid):
    data = {}
    success = True
    if success:
        return jsonify(data), 200
    else:
        return jsonify({}), 200
    
@app.route('/translate/firewall/<productid>', methods=['POST'])
def postLifecycle(productid):
    data = {}
    success = True
    if success:
        return jsonify(data), 200
    else:
        return jsonify({}), 200
    
if __name__ == '__main__':
    initialize()
    context = ('custom.crt', 'custom_cert.key')
    app.run(debug=False, ssl_context=context)