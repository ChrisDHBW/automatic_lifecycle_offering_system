import unittest
from unittest.mock import MagicMock
import LifecycleBroker, ProductDBAdapter, CustomerDBAdapter, OfferingEngineAdapter, CommunicationBrokerAdapter
from Utils import ApiResponse

class TestLifecycleBroker(unittest.TestCase):

    def setUp(self):
        # Set up mock objects for dependencies
        self.mock_product_db = MagicMock(spec=ProductDBAdapter.ProductDBAdapter)
        self.mock_customer_db = MagicMock(spec=CustomerDBAdapter.CustomerDBAdapter)
        self.mock_offering_engine = MagicMock(spec=OfferingEngineAdapter.OfferingEngineAdapter)
        self.mock_communication_broker = MagicMock(spec=CommunicationBrokerAdapter.CommunicationBrokerAdapter)

        # Instanziiere die LifecycleBroker mit den Mock-Objekten
        self.lifecycle_broker = LifecycleBroker()
        self.lifecycle_broker.productDB = self.mock_product_db
        self.lifecycle_broker.customerDB = self.mock_customer_db
        self.lifecycle_broker.offeringEngine = self.mock_offering_engine
        self.lifecycle_broker.communicationBroker = self.mock_communication_broker

    def test_createLifecycleOfferingsForProduct_successful(self):
        # Arrange: Mocks für das Erstellen von Lifecycle-Angeboten
        self.mock_product_db.queryProductData.return_value = ({"id": "1", "name": "Product A"}, True)
        self.mock_offering_engine.createLifecycleOfferings.return_value = True

        # Act: Aufruf der createLifecycleOfferingsForProduct-Methode
        response = self.lifecycle_broker.createLifecycleOfferingsForProduct("1")

        # Assert: Überprüfen, ob createLifecycleOfferings mit dem richtigen Produktaufruf gemacht wurde
        self.assertTrue(response.data)

    def test_createLifecycleOfferingsForProduct_failure(self):
        # Arrange: Mocks für das Scheitern beim Erstellen von Lifecycle-Angeboten
        self.mock_product_db.queryProductData.return_value = (None, False)

        # Act: Aufruf der createLifecycleOfferingsForProduct-Methode
        response = self.lifecycle_broker.createLifecycleOfferingsForProduct("1")

        # Assert: Überprüfen, ob eine fehlerhafte Antwort zurückgegeben wird
        self.assertFalse(response.data)

    def test_getProductData_successful(self):
        # Arrange: Mock für das Abrufen von Produktdaten
        product_data = {"id": "1", "name": "Product A"}
        self.mock_product_db.queryProductData.return_value = (product_data, True)

        # Act: Aufruf der getProductData-Methode
        response = self.lifecycle_broker.getProductData("1")

        # Assert: Überprüfen, ob das richtige Produktdatenobjekt zurückgegeben wird
        self.assertEqual(response.data, product_data)

    def test_getProductData_failure(self):
        # Arrange: Mock für das Scheitern beim Abrufen von Produktdaten
        self.mock_product_db.queryProductData.return_value = (None, False)

        # Act: Aufruf der getProductData-Methode
        response = self.lifecycle_broker.getProductData("1")

        # Assert: Überprüfen, ob eine leere Antwort zurückgegeben wird
        self.assertEqual(response.data, {})

    def test_setProductEndOfLife_successful(self):
        # Arrange: Mock für das Setzen des End-of-Life-Status eines Produkts
        self.mock_product_db.setEndOfLife.return_value = True

        # Act: Aufruf der setProductEndOfLife-Methode
        result = self.lifecycle_broker.setProductEndOfLife("1")

        # Assert: Überprüfen, ob True zurückgegeben wird
        self.assertTrue(result)

    def test_setProductEndOfLife_failure(self):
        # Arrange: Mock für das Scheitern beim Setzen des End-of-Life-Status
        self.mock_product_db.setEndOfLife.return_value = False

        # Act: Aufruf der setProductEndOfLife-Methode
        result = self.lifecycle_broker.setProductEndOfLife("1")

        # Assert: Überprüfen, ob False zurückgegeben wird
        self.assertFalse(result)

    def test_getCustomerWithProduct_successful(self):
        # Arrange: Mock für das Abrufen der Kunden, die das Produkt besitzen
        customers = [{"id": "1", "name": "Customer A"}]
        self.mock_customer_db.queryCustomersByProduct.return_value = (customers, True)

        # Act: Aufruf der getCustomerWithProduct-Methode
        response = self.lifecycle_broker.getCustomerWithProduct("1")

        # Assert: Überprüfen, ob die richtige Kundenliste zurückgegeben wird
        self.assertEqual(response.data, customers)

    def test_getCustomerWithProduct_failure(self):
        # Arrange: Mock für das Scheitern beim Abrufen der Kunden
        self.mock_customer_db.queryCustomersByProduct.return_value = ([], False)

        # Act: Aufruf der getCustomerWithProduct-Methode
        response = self.lifecycle_broker.getCustomerWithProduct("1")

        # Assert: Überprüfen, ob eine leere Liste zurückgegeben wird
        self.assertEqual(response.data, [])

    def test_createOfferings_successful(self):
        # Arrange: Mock für das Erstellen von Angeboten
        self.mock_offering_engine.createOfferings.return_value = True

        # Act: Aufruf der createOfferings-Methode
        result = self.lifecycle_broker.createOfferings()

        # Assert: Überprüfen, ob True zurückgegeben wird
        self.assertTrue(result)

    def test_createOfferings_failure(self):
        # Arrange: Mock für das Scheitern beim Erstellen von Angeboten
        self.mock_offering_engine.createOfferings.return_value = False

        # Act: Aufruf der createOfferings-Methode
        result = self.lifecycle_broker.createOfferings()

        # Assert: Überprüfen, ob False zurückgegeben wird
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
