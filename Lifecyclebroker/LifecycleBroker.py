import ProductDBAdapter, CustomerDBAdapter, OfferingEngineAdapter, CommunicationBrokerAdapter
from Utils import ApiResponse

class LifecycleBroker:

    def __init__(self):
        self.productDB : ProductDBAdapter.ProductDBAdapter = ProductDBAdapter.ProductDBAdapter()
        self.customerDB : CustomerDBAdapter.CustomerDBAdapter = CustomerDBAdapter.CustomerDBAdapter()
        self.offeringEngine : OfferingEngineAdapter.OfferingEngineAdapter = OfferingEngineAdapter.OfferingEngineAdapter()
        self.communicationBroker : CommunicationBrokerAdapter.CommunicationBrokerAdapter = CommunicationBrokerAdapter.CommunicationBrokerAdapter()

    def createLifecycleOfferingsForProduct(self, productId : str) -> ApiResponse.ApiResponse:
        product_data = self.getProductData(productId)
        if not product_data:
            return ApiResponse.ApiResponse(success=False, message="Produkt nicht gefunden.")
        
        # 2. Produkt-Lifecycle-Angebote mit der Offering Engine erstellen
        offering_creation_success = self.offeringEngine.createLifecycleOfferings(product_data)
        if not offering_creation_success:
            return ApiResponse.ApiResponse(success=False, message="Fehler beim Erstellen der Angebote.")
        
        # 3. Kommunikation an Kunden senden, falls gewünscht
        customers = self.getCustomerWithProduct(productId)
        if customers:
            # Nachricht an alle betroffenen Kunden senden
            for customer in customers:
                self.communicationBroker.sendProductLifecycleNotification(customer, productId)
        return ApiResponse.ApiResponse(True)

    def getProductData(self, productId : str) -> dict:
        product_data = self.productDB.getProductById(productId)
        return product_data if product_data else {}

    def setProductEndOfLife(self, productId : str) -> bool:
        update_success = self.productDB.setProductStatus(productId, "End of Life")
        return update_success
        

    def getCustomerWithProduct(self, productId : str) -> list:
        customers = self.customerDB.getCustomersByProductId(productId)
        return customers
        
    def createOfferings(self) -> bool:
        offerings_created = self.offeringEngine.createGeneralOfferings()
        return offerings_created