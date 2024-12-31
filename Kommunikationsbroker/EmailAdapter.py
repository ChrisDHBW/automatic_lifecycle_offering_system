from Utils import Attachment
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import io
import pandas

class EmailAdapter:

    def __init__(self):
        self.serverDomain : str = "<email-server-domain>"
        self.serverPort : int = 0
        self.serverUsername : str = "email-server-username"
        self.serverSecret: str = "email-server-secret"

    def sendEmail(self, targetEmail : str, subject : str, content : str, attachments : list[Attachment.Attachment]) -> bool:
        try:
            # Setup email server connection
            server = smtplib.SMTP(self.serverDomain, self.serverPort)
            server.starttls()
            server.login(self.serverUsername, self.serverSecret)

            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.serverUsername
            msg['To'] = targetEmail
            msg['Subject'] = subject

            # Add email body content
            msg.attach(MIMEText(content, 'plain'))

            # Attach files
            for attachment in attachments:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.content)
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={attachment.filename}')
                msg.attach(part)

            # Send email
            server.send_message(msg)
            server.quit()
            return True

        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def convertAttachmentToExcelFile(self, attachment : Attachment.Attachment) -> dict:
        try:
            # Assuming the attachment is in a CSV format
            csv_data = io.StringIO(attachment.content.decode('utf-8'))
            df = pandas.read_csv(csv_data)
            return df.to_dict()
        except Exception as e:
            print(f"Failed to convert attachment to Excel file: {e}")
            return {}

    def convertAttachmentToBytestream(self, attachment : dict) -> str:
        try:
            # Convert dictionary to a pandas DataFrame
            df = pandas.DataFrame(attachment)
            # Convert DataFrame to a CSV byte stream
            byte_stream = io.BytesIO()
            df.to_csv(byte_stream, index=False)
            byte_stream.seek(0)
            return byte_stream.read().decode('utf-8')
        except Exception as e:
            print(f"Failed to convert data to bytestream: {e}")
            return ""