from Utils import Message, Attachment

class Task(Message):

    def __init__(self):
        super()

    def getTarget(self) -> str:
        return self.targetEmail
    
    def getSubject(self) -> str:
        return self.subject
    
    def getContent(self) -> str:
        return self.content
    
    def getAttachments(self) -> list[Attachment.Attachment]:
        return self.attachments