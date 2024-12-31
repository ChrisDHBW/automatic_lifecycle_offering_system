import CustomerDBAdapter
import TranslationEngineAdapter
import CommunicationBrokerAdapter
from Utils import Message, ApiResponse

class OfferingCalculator:

    def __init__(self):
        self.customerDB : CustomerDBAdapter.CustomerDBAdapter = CustomerDBAdapter.CustomerDBAdapter()
        self.translationEngine : TranslationEngineAdapter.TranslationEngineAdapter = TranslationEngineAdapter.TranslationEngineAdapter()
        self.communicationBroker : CommunicationBrokerAdapter.CommunicationBrokerAdapter = CommunicationBrokerAdapter.CommunicationBrokerAdapter()
        self.offeringItems : list = []
        self.currentCustomerId : str= ""

    def getOfferings(self) -> ApiResponse.ApiResponse:
        offeringlist, success = self.customerDB.queryAllOfferings()
        if success: 
            return self.createJSONResponse(offeringlist)
        else:
            return self.createJSONResponse(False)

    def getOffering(self, offeringId : str) -> ApiResponse.ApiResponse:
        offeringDict, success = self.customerDB.queryAllOffering(offeringId)
        if success: 
            return self.createJSONResponse(offeringDict)
        else:
            return self.createJSONResponse(False)

    def createNewOfferingForCustomer(self, customerId: str, oldProductId : str) -> ApiResponse.ApiResponse:
        self.currentCustomerId = customerId
        orderedAmount, success = self.customerDB.queryAllOrderedProductsByCustomer(customerId, oldProductId)
        if success:
            productDict, success = self.translationEngine.askForNewProduct(customerId, oldProductId)
            self.offeringItems.append({productDict, orderedAmount})
            if success:
                price = self.calculatePrice()
                message = self.writeMessageForTarget()
                success = self.createCommunicationTask(message)
                if success:
                    self.saveOfferingToDatabase()
                    return self.createJSONResponse(True)
                else:
                    return self.createJSONResponse(False)
            else:
                return self.createJSONResponse(False)
        else:
            return self.createJSONResponse(False)
    
    def calculatePrice() -> int:
        pass

    def getOldProductAmountForCustomerById(self, customerId : str, oldProductId : str) -> int:
        orderedAmount, success = self.customerDB.queryAllOrderedProductsByCustomer(customerId, oldProductId)
        if success:
            return orderedAmount
        else:
            return -1

    def createCommunicationTask(self, message : Message.Message) -> bool:
        success = self.communicationBroker.createDelayedMessageTask(message)
        if success:
            return True
        else:
            return False

    def saveOfferingToDatabase(self) -> bool:
        created, success = self.customerDB.addNewOfferingEntryForCustomer(self.currentCustomerId)
        if success:
            return created
        else:
            return False

    def writeMessageForTarget(self) -> Message.Message:
        msg = Message.Message()
        return msg

    def updateOffering(self, offeringId : str, data : dict) -> ApiResponse.ApiResponse:
        success = self.customerDB.updateOfferingEntryForCustomer(offeringId, data)
        if success:
            return True
        else:
            return False

    def createJSONResponse(self, dataObj : dict, dataList : list) -> ApiResponse.ApiResponse:
        if dataObj != None:
            return ApiResponse.ApiResponse(dataObj)
        if dataList != None:
            return ApiResponse.ApiResponse(dataList)
        else:
            ApiResponse.ApiResponse(False)