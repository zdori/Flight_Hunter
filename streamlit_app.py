
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Flight Hunter')
streamlit.header('Welcome to the Flight Hunter app!')
streamlit.text('Below you can see your previously added information:')

def get_user_data():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select username, origin, destination, max_price, period, tier, email, email_noti, phone, sms_noti from USER_PREFERENCES;")
        return my_cur.fetchall()
    
def get_iata_codes():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select concat(airport_name, ' (', iata_code,')') from iata_codes_table;")
        return my_cur.fetchall()

def insert_row_snowflake(username, origin, destination, budget, from_period, to_period, tier, email, email_noti, phone, sms_noti):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into user_preferences (USERNAME, ORIGIN, DESTINATION, MAX_PRICE, PERIOD, TIER, EMAIL, EMAIL_NOTI, PHONE, SMS_NOTI) values ('"+username+"'," 
                       + "'" + origin +"',"
                       + "'" + destination +"',"
                       + "'" + budget + "',"
                       + "'" + min(from_period,to_period) + "," + max(from_period,to_period) + "',"
                       + "'" + tier + "',"
                       + "'" + email + "',"
                       + "'" + email_noti + "',"
                       + "'" + phone + "',"
                       + "'" + sms_noti + "',"
                       "')")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_user_data()
iata_codes = get_iata_codes()
my_cnx.close()
display_data = pandas.DataFrame(my_data_rows)
display_data.columns = ['Username', 'Origin', 'Destination', 'Budget', 'Period', 'Tier', 'E-mail', 'E-mail notification', 'Phone', 'SMS notification']
streamlit.dataframe(display_data)

#if streamlit.button('Add new values'):
username = streamlit.text_input('Username')
origin = streamlit.selectbox('Origin',iata_codes)[-4:-1]
destination = streamlit.selectbox('Destination',iata_codes)[-4:-1]
budget = streamlit.number_input('Budget')
from_period = streamlit.number_input('From Period')
to_period = streamlit.number_input('To Period')
tier = streamlit.selectbox('Tier', ['Basic', 'Standard', 'Premium'])[0]
email = streamlit.text_input('E-mail')
email_noti = streamlit.checkbox('E-mail notification')
phone = streamlit.text_input('Phone')
sms_noti = streamlit.checkbox('SMS notification')
if streamlit.button('Submit'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    insert_row_snowflake()

