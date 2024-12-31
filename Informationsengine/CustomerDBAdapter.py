from Utils import TimeRange
import mysql.connector
from mysql.connector import Error


class CustomerDBAdapter:

    def __init__(self):
        self.dbAddress : str = "<ip-of-db>"
        self.dbPort : int = 3306
        self.dbUser : str = "<username>"
        self.dbSecret : str = "<secret-password>"

    def queryAllCustomers(self) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()
            connection.close()
            return customers, True
        except Error as e:
            print(f"Error querying all customers: {e}")
            return [], False

    def queryCustomerById(self, id : str) -> {dict, bool}:
        try:
            connection = self.connect()
            if not connection:
                return {}, False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM customers WHERE id = %s", (id,))
            customer = cursor.fetchone()
            connection.close()
            return customer, True if customer else {}, False
        except Error as e:
            print(f"Error querying customer with ID {id}: {e}")
            return {}, False

    def addCustomerEntry(self, data : dict) -> {bool, bool}:
        try:
            connection = self.connect()
            if not connection:
                return False, False

            cursor = connection.cursor()
            query = """
                INSERT INTO customers (name, email, phone) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (data['name'], data['email'], data['phone']))
            connection.commit()
            connection.close()
            return True, True
        except Error as e:
            print(f"Error adding customer entry: {e}")
            return False, False

    def updateCustomerEntry(self, id : str, data : dict) -> {bool, bool}:
        try:
            connection = self.connect()
            if not connection:
                return False, False

            cursor = connection.cursor()
            query = """
                UPDATE customers 
                SET name = %s, email = %s, phone = %s
                WHERE id = %s
            """
            cursor.execute(query, (data['name'], data['email'], data['phone'], id))
            connection.commit()
            connection.close()
            return True, True
        except Error as e:
            print(f"Error updating customer with ID {id}: {e}")
            return False, False

    def removeCustomerEntryById(self) -> {bool, bool}:
        try:
            connection = self.connect()
            if not connection:
                return False, False

            cursor = connection.cursor()
            cursor.execute("DELETE FROM customers WHERE id = %s", (id,))
            connection.commit()
            connection.close()
            return True, True
        except Error as e:
            print(f"Error removing customer with ID {id}: {e}")
            return False, False

    def queryAllOfferings(self) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM offerings")
            offerings = cursor.fetchall()
            connection.close()
            return offerings, True
        except Error as e:
            print(f"Error querying all offerings: {e}")
            return [], False

    def queryAllOrderedOfferings(self) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM offerings WHERE status = 'ordered'")
            offerings = cursor.fetchall()
            connection.close()
            return offerings, True
        except Error as e:
            print(f"Error querying all ordered offerings: {e}")
            return [], False

    def queryAllOpenOfferings(self) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM offerings WHERE status = 'open'")
            offerings = cursor.fetchall()
            connection.close()
            return offerings, True
        except Error as e:
            print(f"Error querying all open offerings: {e}")
            return [], False

    def queryAllAcceptedOfferings(self) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM offerings WHERE status = 'accepted'")
            offerings = cursor.fetchall()
            connection.close()
            return offerings, True
        except Error as e:
            print(f"Error querying all accepted offerings: {e}")
            return [], False

    def queryAllDeclinedOfferings(self) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM offerings WHERE status = 'declined'")
            offerings = cursor.fetchall()
            connection.close()
            return offerings, True
        except Error as e:
            print(f"Error querying all declined offerings: {e}")
            return [], False

    def queryAllOfferingsInRange(self, timeRange : TimeRange.TimeRange) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT * FROM offerings 
                WHERE status = 'declined' AND date BETWEEN %s AND %s
            """
            cursor.execute(query, (timeRange.start, timeRange.end))
            offerings = cursor.fetchall()
            connection.close()
            return offerings, True
        except Error as e:
            print(f"Error querying declined offerings in time range: {e}")
            return [], False

    def removeOfferingsRelatedToCustomerById(self, id : str) -> {bool, bool}:
        try:
            connection = self.connect()
            if not connection:
                return False, False

            cursor = connection.cursor()
            cursor.execute("DELETE FROM offerings WHERE customer_id = %s", (id,))
            connection.commit()
            connection.close()
            return True, True
        except Error as e:
            print(f"Error removing offerings related to customer with ID {id}: {e}")
            return False, False

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.dbAddress,
                port=self.dbPort,
                user=self.dbUser,
                password=self.dbSecret,
                database="Customer_DB"
            )
            return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None