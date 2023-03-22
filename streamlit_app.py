
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
        my_cur.execute("select iata_code from iata_codes_table;")
        return my_cur.fetchall()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_user_data()
iata_codes = get_iata_codes()
my_cnx.close()
display_data = pandas.DataFrame(my_data_rows)
display_data.columns = ['Username', 'Origin', 'Destination', 'Budget', 'Period', 'Tier', 'E-mail', 'E-mail notification', 'Phone', 'SMS notification']
streamlit.dataframe(display_data)

elements = [
    streamlit.text_input('Username'),
    streamlit.selectbox('Origin',iata_codes),
    streamlit.selectbox('Destination',iata_codes),
    streamlit.number_input('Budget'),
    streamlit.number_input('From Period'),
    streamlit.number_input('To Period'),
    streamlit.text_input('E-mail'),
    streamlit.checkbox('E-mail notification'),
    streamlit.text_input('Phone'),
    streamlit.checkbox('SMS notification')
]
add_dataframe = pandas.DataFrame(elements)