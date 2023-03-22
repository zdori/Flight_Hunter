
import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

class Snowflake_Connection:
    def create_cursor(self):
        with open("rsa_key.p8", "rb") as key:
            p_key= serialization.load_pem_private_key(
                key.read(),
                password=None,
                backend=default_backend()
            )

        pkb = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())

        ctx = snowflake.connector.connect(
            user='zdori',
            account='lwbcjdb-dg71158',
            private_key=pkb,
            warehouse='COMPUTE_WH',
            database="FLIGHTHUNTER",
            schema="MAIN"
            )

        return ctx.cursor()
    
    def __init__(self):
        self.cursor = self.create_cursor()

