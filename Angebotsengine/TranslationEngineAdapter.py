import requests

class TranslationEngineAdapter:

    def __init__(self):
        self.engineAddress : str = "127.0.0.1"
        self.enginePort : int = 10030

    def askForNewProduct(self, oldProductId : str) -> {dict, bool}:
        url = f"https://{self.engineAddress}:{self.enginePort}/translate/"
        payload = {"oldProductId": oldProductId}
        try:
            response = requests.post(url, json=payload, verify=False)
            response.raise_for_status()
        
            response_data = response.json()
            success = response_data.get("success", False)
            return response_data, success

        except requests.exceptions.RequestException as e:
            print(f"Error while contacting translation engine: {e}")
            return {}, False