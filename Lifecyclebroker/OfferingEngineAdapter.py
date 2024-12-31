import requests

class OfferingEngineAdapter:

    def __init__(self):
        self.engineAddress : str = "127.0.0.1"
        self.enginePort : int = 10020

    def createOfferingForCustomer(self, customerId : str, data : dict) -> {dict, bool}:
        url = f"https://{self.engineAddress}:{self.enginePort}/offering/"
        payload = {"Customer-ID": customerId, "Data" : data}
        try:
            response = requests.post(url, json=payload, verify=False)
            response.raise_for_status()
        
            response_data = response.json()
            success = response_data.get("success", False)
            return response_data, success

        except requests.exceptions.RequestException as e:
            print(f"Error while contacting translation engine: {e}")
            return {}, False