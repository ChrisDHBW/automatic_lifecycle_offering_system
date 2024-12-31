import unittest
from unittest.mock import MagicMock
import DataHandler, ProductDBAdapter, CustomerDBAdapter
from Utils import ApiResponse


class TestDataHandler(unittest.TestCase):

    def setUp(self):
        # Set up mock objects for dependencies
        self.mock_product_db = MagicMock(spec=ProductDBAdapter.ProductDBAdapter)
        self.mock_customer_db = MagicMock(spec=CustomerDBAdapter.CustomerDBAdapter)
        
        # Instanziiere die DataHandler mit den Mock-Objekten
        self.data_handler = DataHandler()
        self.data_handler.productDB = self.mock_product_db
        self.data_handler.customerDB = self.mock_customer_db

    def test_getCustomers_returns_successful_response(self):
        # Arrange: Mock für die Rückgabe von Kunden
        customers = [{"id": "1", "name": "John Doe"}]
        self.mock_customer_db.queryAllCustomers.return_value = (customers, True)

        # Act: Aufruf der getCustomers-Methode
        response = self.data_handler.getCustomers()

        # Assert: Überprüfen, ob createJSONResponse mit der richtigen Liste aufgerufen wurde
        self.assertEqual(response.data, customers)

    def test_getCustomer_returns_successful_response(self):
        # Arrange: Mock für die Rückgabe eines einzelnen Kunden
        customer = {"id": "1", "name": "John Doe"}
        self.mock_customer_db.queryCustomerById.return_value = (customer, True)

        # Act: Aufruf der getCustomer-Methode
        response = self.data_handler.getCustomer("1")

        # Assert: Überprüfen, ob createJSONResponse mit dem richtigen Kunden aufgerufen wurde
        self.assertEqual(response.data, customer)

    def test_addCustomer_returns_true_on_success(self):
        # Arrange: Mock für das Hinzufügen eines Kunden
        self.mock_customer_db.addCustomerEntry.return_value = (True, True)

        # Act: Aufruf der addCustomer-Methode
        result = self.data_handler.addCustomer({"name": "John Doe"})

        # Assert: Überprüfen, ob der Kunde erfolgreich hinzugefügt wurde
        self.assertTrue(result)

    def test_addCustomer_returns_false_on_failure(self):
        # Arrange: Mock für das Hinzufügen eines Kunden, das fehlschlägt
        self.mock_customer_db.addCustomerEntry.return_value = (False, False)

        # Act: Aufruf der addCustomer-Methode
        result = self.data_handler.addCustomer({"name": "John Doe"})

        # Assert: Überprüfen, ob das Hinzufügen fehlschlägt
        self.assertFalse(result)

    def test_updateCustomer_returns_true_on_success(self):
        # Arrange: Mock für das Aktualisieren eines Kunden
        self.mock_customer_db.updateCustomerEntry.return_value = (True, True)

        # Act: Aufruf der updateCustomer-Methode
        result = self.data_handler.updateCustomer("1", {"name": "John Doe"})

        # Assert: Überprüfen, ob der Kunde erfolgreich aktualisiert wurde
        self.assertTrue(result)

    def test_updateCustomer_returns_false_on_failure(self):
        # Arrange: Mock für das Aktualisieren eines Kunden, das fehlschlägt
        self.mock_customer_db.updateCustomerEntry.return_value = (False, False)

        # Act: Aufruf der updateCustomer-Methode
        result = self.data_handler.updateCustomer("1", {"name": "John Doe"})

        # Assert: Überprüfen, ob das Aktualisieren fehlschlägt
        self.assertFalse(result)

    def test_getProducts_returns_successful_response(self):
        # Arrange: Mock für die Rückgabe von Produkten
        products = [{"id": "1", "name": "Product A"}]
        self.mock_product_db.queryAllProducts.return_value = (products, True)

        # Act: Aufruf der getProducts-Methode
        response = self.data_handler.getProducts()

        # Assert: Überprüfen, ob createJSONResponse mit der richtigen Produktliste aufgerufen wurde
        self.assertEqual(response.data, products)

    def test_calculateStatistics_returns_data_on_success(self):
        # Arrange: Mock für das Abfragen von Offering-Daten
        offerings = [{"id": "1", "status": "accepted"}]
        self.mock_customer_db.queryAllOfferings.return_value = (offerings, True)

        # Act: Aufruf der calculateStatistics-Methode
        result = self.data_handler.calculateStatistics()

        # Assert: Überprüfen, ob alle Angebote zurückgegeben werden
        self.assertEqual(result, offerings)

    def test_summarizeSystem_returns_data_on_success(self):
        # Arrange: Mock für das Abfragen von Angeboten
        offerings = [{"id": "1", "status": "ordered"}]
        self.mock_customer_db.queryAllOfferingsInRange.return_value = (offerings, True)

        # Act: Aufruf der summarizeSystem-Methode
        result = self.data_handler.summarizeSystem()

        # Assert: Überprüfen, ob die letzten vier Wochen Angebote zurückgegeben werden
        self.assertEqual(result, offerings)

if __name__ == '__main__':
    unittest.main()