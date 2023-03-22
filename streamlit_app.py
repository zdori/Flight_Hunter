
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
        my_cur.execute("select username, origin, destination, max_price from USER_PREFERENCES;")
        return my_cur.fetchall()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_user_data()
my_cnx.close()
streamlit.dataframe(my_data_rows)