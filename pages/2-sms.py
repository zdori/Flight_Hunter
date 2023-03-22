# Run:
# pip3 install twilio

import os
import streamlit
from twilio.rest import Client
import snowflake.connector

numbers_to_message = ['+36307763909', '+36307763909']

def get_user_data():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select username, tier, email_noti, sms_noti, email, phone  from USER_PREFERENCES;")
        return my_cur.fetchall()

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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_user_data()
my_cnx.close()

streamlit.text(my_data_rows)

send_sms = filter(lambda row: row[3], my_data_rows)
streamlit.text(send_sms)

tier_p = filter(lambda row: row[1] == 'P', my_data_rows)
streamlit.text(f'Premium users: {tier_p}')

tier_s = filter(lambda row: row[1] == 'S', my_data_rows)
streamlit.text(f'Standard users: {tier_s}')

tier_b = filter(lambda row: row[1] == 'B', my_data_rows)
streamlit.text(f'Basic users: {tier_b}')




is_clicked = streamlit.button('Send Test SMS')

if is_clicked:
    r = send_sms('Hello, Bob!', ['+36307763909', '+36307763909'])
    streamlit.text(f'Result: {r}')


# New numbers has to be added and verirfied on twilio's website