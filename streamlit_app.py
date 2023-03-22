
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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_user_data()
my_cnx.close()
display_data = pandas.DataFrame(my_data_rows)
display_data.columns = ['Username', 'Origin', 'Destination', 'Budget', 'Period', 'Tier', 'E-mail', 'E-mail notification', 'Phone', 'SMS notification']
streamlit.dataframe(display_data)