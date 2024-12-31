import ProductDBAdapter
import CustomerDBAdapter
import json
from Utils import ApiResponse


class DataHandler:

    def __init__(self):
        self.productDB : ProductDBAdapter.ProductDBAdapter = ProductDBAdapter.ProductDBAdapter()
        self.customerDB : CustomerDBAdapter.CustomerDBAdapter = CustomerDBAdapter.CustomerDBAdapter()

    def getCustomers(self) -> list:
        list, success = self.customerDB.queryAllCustomers()
        if success:
            return self.createJSONResponse(None, list)
        else:
            return self.createJSONResponse(None, [])

    def getCustomer(self, id : str) -> dict:
        dict, success = self.customerDB.queryCustomerById(id)
        if success:
            return self.createJSONResponse(dict, None)
        else:
            return self.createJSONResponse({}, None)

    def addCustomer(self, data : dict) -> bool:
        added, success = self.customerDB.addCustomerEntry(data)
        if success:
            return added
        else:
            return False

    def updateCustomer(self, id : str, newData : dict) -> bool:
        updated, success = self.customerDB.updateCustomerEntry(id, newData)
        if success:
            return updated
        else:
            return False

    def deleteCustomer(self, id : str) -> bool:
        offeringDeleteSuccess = self.deleteOfferingsForCustomerById(id)
        deleted, success = self.customerDB.removeCustomerEntryById(id)
        if success and offeringDeleteSuccess:
            return deleted
        else:
            return False

    def deleteOfferingsForCustomerById(self, id : str) -> bool:
        self.customerDB.removeOfferingsRelatedToCustomerById(id)

    def getProducts(self) -> list:
        list, success = self.productDB.queryAllProducts()
        if success:
            return self.createJSONResponse(None, list)
        else:
            return self.createJSONResponse(None, [])

    def getProduct(self, id : str) -> dict:
        dict, success = self.productDB.queryProductWithId(id)
        if success:
            return self.createJSONResponse(dict, None)
        else:
            return self.createJSONResponse({}, None)
    
    def addProduct(self, data : dict) -> bool:
        added, success = self.productDB.addProductEntry(data)
        if success:
            return added
        else:
            return False

    def updateProduct(self, id : str, newData : dict) -> bool:
        updated, success = self.productDB.updateProductEntry(id, newData)
        if success:
            return updated
        else:
            return False

    def calculateStatistics(self) -> dict:
        acceptedOffering, success = self.customerDB.queryAllAcceptedOfferings()
        declinedOffering, success = self.customerDB.queryAllDeclinedOfferings()
        openOffering, success = self.customerDB.queryAllOpenOfferings()
        allOffering, success = self.customerDB.queryAllOfferings()
        if success:
            return allOffering
        else:
            return []

    def summarizeSystem(self) -> dict:
        orderedOffering, success = self.customerDB.queryAllOrderedOfferings()
        lastFourWeeksOffering, success = self.customerDB.queryAllOfferingsInRange()
        if success:
            return lastFourWeeksOffering
        else:
            return []

    def createJSONResponse(self, dataObj : dict, dataList : list) -> ApiResponse.ApiResponse:
        if dataObj != None:
            return ApiResponse.ApiResponse(dataObj)
        if dataList != None:
            return ApiResponse.ApiResponse(dataList)
        else:
            ApiResponse.ApiResponse(False)
    