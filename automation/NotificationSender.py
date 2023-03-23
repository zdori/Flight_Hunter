from email.message import EmailMessage
import ssl
import smtplib
#from twilio.rest import Client
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

class NotificationSender(object):

    def __init__(self, user_data, api_suggestion):
        self.user_data = user_data
        self.api_suggestion = api_suggestion
    
   # def send_sms(self):
   #     account_sid = "AC758e32bf8cfd2a044eb06fda71874bbc"
   #     auth_token = "74fccbb9d92c786a8da4195048cc541a"
   #     client = Client(account_sid, auth_token)
   #     text_msg = f'Hi, {self.user_data.username}!'
   #     respone = client.messages.create(
   #     body = text_msg,
   #         from_ = '+15155828709',
   #         to = self.user_data.phone
   #     )
   #     return respone.status
    
    def send_mail(self, subject, body):
        email_sender = 'SchemaFlightHunters@gmail.com'
        email_password = 'cwcanuqotlsvudnu'
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = self.user_data.email
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, self.user_data.email, em.as_string())
