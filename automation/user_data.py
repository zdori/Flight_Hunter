import snowflake_connection as sc

class User_Preferences_Table(sc.Snowflake_Connection):
    def getData(self):
        sqlCommand = """
        select USERNAME, DESTINATION, MAX_PRICE, PERIOD, ORIGIN, PRICE_THRESHOLD, TIER, EMAIL_NOTI, SMS_NOTI, EMAIL, PHONE from USER_PREFERENCES;
        """
        rows = super().create_cursor().execute(sqlCommand).fetchall()
        return list(map(User_Data, rows))
    
    def __init__(self):
        super().__init__()
        self.data = self.getData()

class User_Data:
    def __init__(self, row):
        self.row = row
        self.username = row[0]
        self.destination = row[1]
        self.max_price = row[2]
        self.period = row[3]
        self.origin = row[4]
        self.price_threshold = row[5]
        self.tier = row[6]
        self.email_noti = row[7]
        self.sms_noti = row[8]
        self.email = row[9]
        self.phone = row[10]
    
    def __repr__(self):
        rowstr = ','.join(str(v) for v in self.row)
        return f'User_Data({rowstr})'
    
        
     
