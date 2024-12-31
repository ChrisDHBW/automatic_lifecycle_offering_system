import mysql.connector
from mysql.connector import Error
import Offering


class CustomerDBAdapter:

    def __init__(self):
        self.dbAddress : str = "<ip-of-db>"
        self.dbPort : int = 3306
        self.dbUser : str = "<username>"
        self.dbSecret : str = "<secret-password>"

    def queryAllOrderedProductsByCustomer(self, customerId : str, productId : str) -> {int, bool}:
        connection = self.connect()
        if not connection:
            return (0, False)

        try:
            cursor = connection.cursor()
            query = """
                SELECT COUNT(*) FROM Orders
                WHERE customer_id = %s AND product_id = %s;
            """
            cursor.execute(query, (customerId, productId))
            result = cursor.fetchone()
            return (result[0] if result else 0, True)
        except Error as e:
            print(f"Error querying ordered products: {e}")
            return (0, False)
        finally:
            connection.close()

    def queryAllOfferings(self) -> {list, bool}:
        connection = self.connect()
        if not connection:
            return (0, False)

        try:
            cursor = connection.cursor()
            query = """
                SELECT COUNT(*) FROM Orders
                WHERE customer_id = %s AND product_id = %s;
            """
            cursor.execute(query)
            result = cursor.fetchone()
            return (result[0] if result else 0, True)
        except Error as e:
            print(f"Error querying ordered products: {e}")
            return (0, False)
        finally:
            connection.close()

    def queryAllOffering(self, offeringId : str) -> {dict, bool}:
        connection = self.connect()
        if not connection:
            return (0, False)

        try:
            cursor = connection.cursor()
            query = """
                SELECT COUNT(*) FROM Orders
                WHERE customer_id = %s AND product_id = %s;
            """
            cursor.execute(query)
            result = cursor.fetchone()
            return (result[0] if result else 0, True)
        except Error as e:
            print(f"Error querying ordered products: {e}")
            return (0, False)
        finally:
            connection.close()

    def addNewOfferingEntryForCustomer(self, customerId : str, offeringData : Offering.Offering) -> {bool, bool}:
        connection = self.connect()
        if not connection:
            return (0, False)

        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Offerings (customer_id, offering_name, offering_price, offering_date)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (customerId, offeringData.name, offeringData.price, offeringData.date))
            connection.commit()
            return (cursor.lastrowid, True)
        except Error as e:
            print(f"Error adding new offering: {e}")
            return (0, False)
        finally:
            connection.close()

    def updateOfferingEntryForCustomer(self, customerId : str, newOfferingData : Offering.Offering) -> {int, bool}:
        connection = self.connect()
        if not connection:
            return (0, False)

        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Offerings (customer_id, offering_name, offering_price, offering_date)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (customerId, newOfferingData.name, newOfferingData.price, newOfferingData.date))
            connection.commit()
            return (cursor.lastrowid, True)
        except Error as e:
            print(f"Error adding new offering: {e}")
            return (0, False)
        finally:
            connection.close()

    def queryCustomerContactInformation(self, customerId : str) -> {dict, bool}:
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
                database="Customer_DB"
            )
            return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None