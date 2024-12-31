from Utils import Attachment

class Message:
    
    def __init__(self):
        self.targetEmail : str
        self.subject : str
        self.content : str
        self.attachments : list[Attachment.Attachment]