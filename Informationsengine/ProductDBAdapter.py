import mysql.connector
from mysql.connector import Error

class ProductDBAdapter:

    def __init__(self):
        self.dbAddress : str = "<ip-of-db>"
        self.dbPort : int = 3306
        self.dbUser : str = "<username>"
        self.dbSecret : str = "<secret-password>"

    def queryAllProducts(self) -> {list, bool}:
        try:
            connection = self.connect()
            if not connection:
                return [], False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            connection.close()
            return products, True
        except Error as e:
            print(f"Error querying all products: {e}")
            return [], False

    def queryProductWithId(self, id : str) -> {dict, bool}:
        try:
            connection = self.connect()
            if not connection:
                return {}, False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            product = cursor.fetchone()
            connection.close()
            return product, True if product else {}, False
        except Error as e:
            print(f"Error querying product with ID {id}: {e}")
            return {}, False


    def addProductEntry(self,data : dict) -> {bool, bool}:
        try:
            connection = self.connect()
            if not connection:
                return False, False

            cursor = connection.cursor()
            query = """
                INSERT INTO products (name, price, stock) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (data['name'], data['price'], data['stock']))
            connection.commit()
            connection.close()
            return True, True
        except Error as e:
            print(f"Error adding product entry: {e}")
            return False, False

    def updateProductEntry(self, id : str, newData : dict) -> {bool, bool}:
        try:
            connection = self.connect()
            if not connection:
                return False, False

            cursor = connection.cursor()
            query = """
                UPDATE products 
                SET name = %s, price = %s, stock = %s
                WHERE id = %s
            """
            cursor.execute(query, (newData['name'], newData['price'], newData['stock'], id))
            connection.commit()
            connection.close()
            return True, True
        except Error as e:
            print(f"Error updating product with ID {id}: {e}")
            return False, False


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