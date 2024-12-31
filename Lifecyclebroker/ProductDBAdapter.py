import mysql.connector
from mysql.connector import Error

class ProductDBAdapter:

    def __init__(self):
        self.dbAddress : str = "<ip-of-db>"
        self.dbPort : int = 3306
        self.dbUser : str = "<username>"
        self.dbSecret : str = "<secret-password>"

    def queryProductWithId(self, type : int, customerId : str) -> {dict, bool}:
        connection = self.connect()
        if not connection:
            return ({}, False)

        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT name, email, phone FROM Customers
                WHERE customer_id = %s;
            """
            cursor.execute(query, (customerId,))
            result = cursor.fetchone()
            return (result if result else {}, True)
        except Error as e:
            print(f"Error querying customer contact information: {e}")
            return ({}, False)
        finally:
            connection.close()

    def updateProductWithId(self, type : int, customerId : str, newData : dict) -> {bool, bool}:
        connection = self.connect()
        if not connection:
            return ({}, False)

        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT name, email, phone FROM Customers
                WHERE customer_id = %s;
            """
            cursor.execute(query, (customerId,))
            result = cursor.fetchone()
            return (result if result else {}, True)
        except Error as e:
            print(f"Error querying customer contact information: {e}")
            return ({}, False)
        finally:
            connection.close()

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.dbAddress,
                port=self.dbPort,
                user=self.dbUser,
                password=self.dbSecret,
                database="Product_DB"
            )
            return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None