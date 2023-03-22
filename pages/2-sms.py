# Run:
# pip3 install twilio

import os
import streamlit
from twilio.rest import Client
import snowflake.connector
from apscheduler.schedulers.blocking import BlockingScheduler
from email.message import EmailMessage
import ssl
import smtplib

numbers_to_message = ['+36307763909', '+36307763909']

def get_user_data():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select username, tier, email_noti, sms_noti, email, phone  from USER_PREFERENCES;")
        return my_cur.fetchall()

def send_sms(users):
    account_sid = "AC758e32bf8cfd2a044eb06fda71874bbc"
    auth_token = "74fccbb9d92c786a8da4195048cc541a"
    client = Client(account_sid, auth_token)
    for user in users:
        text_msg = f'Hi, {user[0]}!'
        streamlit.text(text_msg)
        respone = client.messages.create(
            body=text_msg,
            from_='+15155828709',
            to=user[5]
        )
    return respone.status

def send_mail(email_receiver, subject, body):
    email_sender = 'SchemaFlightHunters@gmail.com'
    email_password = 'cwcanuqotlsvudnu'
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_user_data()
my_cnx.close()

streamlit.text(my_data_rows)

user_sms = set(filter(lambda row: row[3], my_data_rows))
user_email = set(filter(lambda row: row[2], my_data_rows))

streamlit.dataframe(user_sms)

tier_p = set(filter(lambda row: row[1] == 'P', my_data_rows))
streamlit.text(f'Premium users: {tier_p}')

tier_s = set(filter(lambda row: row[1] == 'S', my_data_rows))
streamlit.text(f'Standard users: {tier_s}')

tier_b = set(filter(lambda row: row[1] == 'B', my_data_rows))
streamlit.text(f'Basic users: {tier_b}')

sms_p = user_sms.intersection(tier_p)
sms_s = user_sms.intersection(tier_s)
sms_b = user_sms.intersection(tier_b)

email_p = user_email.intersection(tier_p)
email_s = user_email.intersection(tier_s)
email_b = user_email.intersection(tier_b)

"""
scheduler = BlockingScheduler()
scheduler.add_job(send_sms(sms_p), 'interval', hours=1)
scheduler.start()
"""

is_sms_clicked = streamlit.button('Send Test SMS')

if is_sms_clicked:
   # streamlit.text("Users with Premium tier, asking for SMS: " + sms_p)
    r = send_sms(sms_p)
    streamlit.text(f'Result: {r}')

is_email_clicked = streamlit.button('Send Test Email')

if is_email_clicked:
   # streamlit.text("Users with Premium tier, asking for email: " + email_p)
    for user in email_p:
        streamlit.text(user[0] + " " + user[4]);
        body="""
        Hi {user[0]}!

        These are the flights we found for you: 

        Regards,
        FlightHunters
        """
        send_mail(user[4], "Your daily FlightHunter", body)





# New numbers has to be added and verirfied on twilio's website