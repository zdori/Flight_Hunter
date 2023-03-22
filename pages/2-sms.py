# Run:
# pip3 install twilio

import os
import streamlit
from twilio.rest import Client

numbers_to_message = ['+36307763909', '+36307763909']

def send_sms(text_msg='Hello from my Twilio number!', phone_nums=numbers_to_message):
    account_sid = "AC758e32bf8cfd2a044eb06fda71874bbc"
    auth_token = "74fccbb9d92c786a8da4195048cc541a"
    client = Client(account_sid, auth_token)
    for ind,number in enumerate(phone_nums):
        print(f'{ind}: {number}')
        respone = client.messages.create(
            body=text_msg,
            from_='+15155828709',
            to=number
        )
    return respone.status

is_clicked = streamlit.button('Send SMS')

if is_clicked:
    r = send_sms('Hello, Bob!', ['+36307763909', '+36307763909'])
    streamlit.text(f'Result: {r}')


# New numbers has to be added and verirfied on twilio's website