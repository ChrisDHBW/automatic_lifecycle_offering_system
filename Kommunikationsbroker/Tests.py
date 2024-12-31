import unittest
from unittest.mock import MagicMock
import CommunicationHandler, EmailAdapter, CommunicationQueue
from Utils import ApiResponse

class TestCommunicationHandler(unittest.TestCase):

    def setUp(self):
        # Set up mock objects for dependencies
        self.mock_email_adapter = MagicMock(spec=EmailAdapter.EmailAdapter)
        self.mock_queue = MagicMock(spec=CommunicationQueue.CommunicationQueue)
        
        # Instanziiere die CommunicationHandler mit den Mock-Objekten
        self.communication_handler = CommunicationHandler()
        self.communication_handler.emailAdapter = self.mock_email_adapter
        self.communication_handler.queue = self.mock_queue

    def test_communicateNow_calls_sendEmail(self):
        # Arrange: Die erwarteten Parameter für die Email
        msgParams = {"to": "test@example.com", "subject": "Test", "body": "Test message"}
        
        # Act: Aufruf der communicateNow-Methode
        self.communication_handler.communicateNow(msgParams)
        
        # Assert: Überprüfen, ob sendEmail mit den richtigen Parametern aufgerufen wurde
        self.mock_email_adapter.sendEmail.assert_called_once_with("", "", "", [])

    def test_communicateLater_adds_task_to_queue(self):
        # Arrange: Die erwarteten Parameter für die Nachricht
        msgParams = {"to": "test@example.com", "subject": "Test", "body": "Test message"}
        
        # Act: Aufruf der communicateLater-Methode
        self.communication_handler.communicateLater(msgParams)
        
        # Assert: Überprüfen, ob addTaskToQueue mit den richtigen Parametern aufgerufen wurde
        self.mock_queue.addTaskToQueue.assert_called_once_with(msgParams)

if __name__ == '__main__':
    unittest.main()