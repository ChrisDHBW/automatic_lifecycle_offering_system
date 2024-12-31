import requests
from Utils import Message

class CommunicationBrokerAdapter:

    def __init__(self):
        self.brokerAddress : str = "127.0.0.1"
        self.brokerPort : int = 10040

    def createInstantMessageTask(self, msg : Message.Message) -> bool:
        url = f"{self.brokerAddress}:{self.brokerPort}/communicate/now"
        payload = {
            "recipient": msg.recipient,
            "content": msg.content,
            "timestamp": msg.timestamp
        }
        try:
            response = requests.post(url, json=payload, verify=False)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Fehler beim Senden der sofortigen Nachricht: {e}")
            return False

    def createDelayedMessageTask(self, msg : Message.Message) -> bool:
        url = f"{self.brokerAddress}:{self.brokerPort}/communicate/later"
        payload = {
            "recipient": msg.recipient,
            "content": msg.content,
            "sendAt": msg.send_at  # Zeit, zu der die Nachricht gesendet werden soll
        }
        try:
            response = requests.post(url, json=payload, verify=False)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Fehler beim Planen der verzögerten Nachricht: {e}")
            return False