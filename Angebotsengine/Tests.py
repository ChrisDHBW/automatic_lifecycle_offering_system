import unittest
from unittest.mock import MagicMock
import OfferingCalculator, CustomerDBAdapter, TranslationEngineAdapter, CommunicationBrokerAdapter
from Utils import ApiResponse, Message


class TestOfferingCalculator(unittest.TestCase):

    def setUp(self):
        # Set up mock objects for dependencies
        self.mock_customer_db = MagicMock(spec=CustomerDBAdapter.CustomerDBAdapter)
        self.mock_translation_engine = MagicMock(spec=TranslationEngineAdapter.TranslationEngineAdapter)
        self.mock_communication_broker = MagicMock(spec=CommunicationBrokerAdapter.CommunicationBrokerAdapter)
        
        # Instanziiere die OfferingCalculator mit den Mock-Objekten
        self.offering_calculator = OfferingCalculator()
        self.offering_calculator.customerDB = self.mock_customer_db
        self.offering_calculator.translationEngine = self.mock_translation_engine
        self.offering_calculator.communicationBroker = self.mock_communication_broker

    def test_getOfferings_returns_successful_response(self):
        # Arrange: Mock für das Abfragen der Angebote
        offerings = [{"id": "1", "product": "Product A"}]
        self.mock_customer_db.queryAllOfferings.return_value = (offerings, True)

        # Act: Aufruf der getOfferings-Methode
        response = self.offering_calculator.getOfferings()

        # Assert: Überprüfen, ob createJSONResponse mit der richtigen Liste aufgerufen wurde
        self.assertEqual(response.data, offerings)

    def test_getOffering_returns_successful_response(self):
        # Arrange: Mock für das Abfragen eines einzelnen Angebots
        offering = {"id": "1", "product": "Product A"}
        self.mock_customer_db.queryAllOffering.return_value = (offering, True)

        # Act: Aufruf der getOffering-Methode
        response = self.offering_calculator.getOffering("1")

        # Assert: Überprüfen, ob createJSONResponse mit dem richtigen Angebot aufgerufen wurde
        self.assertEqual(response.data, offering)

    def test_createNewOfferingForCustomer_successful(self):
        # Arrange: Mocks für das Erstellen eines neuen Angebots
        self.mock_customer_db.queryAllOrderedProductsByCustomer.return_value = (10, True)
        self.mock_translation_engine.askForNewProduct.return_value = ({"product": "Product B"}, True)
        self.offering_calculator.offeringItems = []

        # Mock für das Berechnen des Preises
        self.offering_calculator.calculatePrice = MagicMock(return_value=100)

        # Mock für das Erstellen der Kommunikationsaufgabe
        self.mock_communication_broker.createDelayedMessageTask.return_value = True

        # Mock für das Speichern des Angebots
        self.mock_customer_db.addNewOfferingEntryForCustomer.return_value = (True, True)

        # Act: Aufruf der createNewOfferingForCustomer-Methode
        response = self.offering_calculator.createNewOfferingForCustomer("customerId", "oldProductId")

        # Assert: Überprüfen, ob createJSONResponse mit True aufgerufen wurde
        self.assertEqual(response.data, True)

    def test_createNewOfferingForCustomer_failure(self):
        # Arrange: Mocks für das Erstellen eines neuen Angebots, das fehlschlägt
        self.mock_customer_db.queryAllOrderedProductsByCustomer.return_value = (10, False)

        # Act: Aufruf der createNewOfferingForCustomer-Methode
        response = self.offering_calculator.createNewOfferingForCustomer("customerId", "oldProductId")

        # Assert: Überprüfen, ob createJSONResponse mit False aufgerufen wurde
        self.assertEqual(response.data, False)

    def test_getOldProductAmountForCustomerById_returns_amount(self):
        # Arrange: Mock für das Abfragen der Bestellmenge eines alten Produkts
        self.mock_customer_db.queryAllOrderedProductsByCustomer.return_value = (10, True)

        # Act: Aufruf der getOldProductAmountForCustomerById-Methode
        amount = self.offering_calculator.getOldProductAmountForCustomerById("customerId", "oldProductId")

        # Assert: Überprüfen, ob die Menge zurückgegeben wurde
        self.assertEqual(amount, 10)

    def test_createCommunicationTask_successful(self):
        # Arrange: Mock für das Erstellen einer Kommunikationsaufgabe
        message = MagicMock(spec=Message.Message)
        self.mock_communication_broker.createDelayedMessageTask.return_value = True

        # Act: Aufruf der createCommunicationTask-Methode
        result = self.offering_calculator.createCommunicationTask(message)

        # Assert: Überprüfen, ob True zurückgegeben wurde
        self.assertTrue(result)

    def test_createCommunicationTask_failure(self):
        # Arrange: Mock für das Erstellen einer Kommunikationsaufgabe, das fehlschlägt
        message = MagicMock(spec=Message.Message)
        self.mock_communication_broker.createDelayedMessageTask.return_value = False

        # Act: Aufruf der createCommunicationTask-Methode
        result = self.offering_calculator.createCommunicationTask(message)

        # Assert: Überprüfen, ob False zurückgegeben wurde
        self.assertFalse(result)

    def test_saveOfferingToDatabase_successful(self):
        # Arrange: Mock für das Speichern des Angebots
        self.mock_customer_db.addNewOfferingEntryForCustomer.return_value = (True, True)

        # Act: Aufruf der saveOfferingToDatabase-Methode
        result = self.offering_calculator.saveOfferingToDatabase()

        # Assert: Überprüfen, ob True zurückgegeben wurde
        self.assertTrue(result)

    def test_saveOfferingToDatabase_failure(self):
        # Arrange: Mock für das Speichern des Angebots, das fehlschlägt
        self.mock_customer_db.addNewOfferingEntryForCustomer.return_value = (False, False)

        # Act: Aufruf der saveOfferingToDatabase-Methode
        result = self.offering_calculator.saveOfferingToDatabase()

        # Assert: Überprüfen, ob False zurückgegeben wurde
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
