import EmailAdapter, CommunicationQueue
from Utils import ApiResponse

class CommunicationHandler:

    def __init__(self):
        self.emailAdapter : EmailAdapter.EmailAdapter = EmailAdapter.EmailAdapter()
        self.queue : CommunicationQueue.CommunicationQueue = CommunicationQueue.CommunicationQueue()

    def communicateNow(self, msgParams : dict) -> ApiResponse:
        self.emailAdapter.sendEmail("", "", "", [])

    def communicateLater(self, msgParams : dict) -> ApiResponse:
        self.queue.addTaskToQueue(msgParams)