import ProductDBAdapter, CustomerDBAdapter, OfferingEngineAdapter, CommunicationBrokerAdapter
from Utils import ApiResponse

class LifecycleBroker:

    def __init__(self):
        self.productDB : ProductDBAdapter.ProductDBAdapter = ProductDBAdapter.ProductDBAdapter()
        self.customerDB : CustomerDBAdapter.CustomerDBAdapter = CustomerDBAdapter.CustomerDBAdapter()
        self.offeringEngine : OfferingEngineAdapter.OfferingEngineAdapter = OfferingEngineAdapter.OfferingEngineAdapter()
        self.communicationBroker : CommunicationBrokerAdapter.CommunicationBrokerAdapter = CommunicationBrokerAdapter.CommunicationBrokerAdapter()

    def createLifecycleOfferingsForProduct(productId : str) -> ApiResponse.ApiResponse:
        pass

    def getProductData(productId : str) -> dict:
        pass

    def setProductEndOfLife(productId : str) -> bool:
        pass

    def getCustomerWithProduct(productId : str) -> list:
        pass

    def createOfferings() -> bool:
        pass