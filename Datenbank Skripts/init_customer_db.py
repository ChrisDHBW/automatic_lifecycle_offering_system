import mysql.connector
from mysql.connector import errorcode

# Datenbank-Konfigurationsparameter
DB_NAME = "CustomerDatabase"
TABLES = {}

# Tabellenstruktur basierend auf dem Diagramm
TABLES['Customer'] = (
    "CREATE TABLE Customer ("
    "  Customer_ID INT AUTO_INCREMENT PRIMARY KEY,"
    "  Name VARCHAR(255) NOT NULL,"
    "  Branche VARCHAR(255),"
    "  Contact VARCHAR(255),"
    "  AccountManager VARCHAR(255),"
    "  OfferingPreference VARCHAR(255)"
    ")"
)

TABLES['Offering'] = (
    "CREATE TABLE Offering ("
    "  Offering_ID INT AUTO_INCREMENT PRIMARY KEY,"
    "  Customer_ID INT,"
    "  Titel VARCHAR(255),"
    "  Preis DECIMAL(10,2),"
    "  Status VARCHAR(255),"
    "  Versanddatum DATE,"
    "  Kommentar TEXT,"
    "  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)"
    ")"
)

TABLES['OfferingItem'] = (
    "CREATE TABLE OfferingItem ("
    "  Offering_Item_ID INT AUTO_INCREMENT PRIMARY KEY,"
    "  Offering_ID INT,"
    "  Product_ID INT,"
    "  Product_Name VARCHAR(255),"
    "  Amount INT,"
    "  Preis DECIMAL(10,2),"
    "  Kommentar TEXT,"
    "  FOREIGN KEY (Offering_ID) REFERENCES Offering(Offering_ID)"
    ")"
)

TABLES['InstalledBase'] = (
    "CREATE TABLE InstalledBase ("
    "  Installed_Base_ID INT AUTO_INCREMENT PRIMARY KEY,"
    "  Customer_ID INT,"
    "  Product_ID INT,"
    "  Amount INT,"
    "  Preis DECIMAL(10,2),"
    "  Kommentar TEXT,"
    "  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)"
    ")"
)

TABLES['IB_Offering_Zuordnung'] = (
    "CREATE TABLE IB_Offering_Zuordnung ("
    "  ZuordnungsID INT AUTO_INCREMENT PRIMARY KEY,"
    "  Installed_Base_ID INT,"
    "  Offering_ID INT,"
    "  FOREIGN KEY (Installed_Base_ID) REFERENCES InstalledBase(Installed_Base_ID),"
    "  FOREIGN KEY (Offering_ID) REFERENCES Offering(Offering_ID)"
    ")"
)

TABLES['Alt_Neu_Zuordnung'] = (
    "CREATE TABLE Alt_Neu_Zuordnung ("
    "  ZuordnungsID INT AUTO_INCREMENT PRIMARY KEY,"
    "  Installed_Base_ID INT,"
    "  Offering_Item_ID INT,"
    "  FOREIGN KEY (Installed_Base_ID) REFERENCES InstalledBase(Installed_Base_ID),"
    "  FOREIGN KEY (Offering_Item_ID) REFERENCES OfferingItem(Offering_Item_ID)"
    ")"
)

# Verbindung zur MySQL-Datenbank herstellen
def connect_to_database():
    try:
        cnx = mysql.connector.connect(
            user='your_username',  # Benutzername hier eingeben
            password='your_password'  # Passwort hier eingeben
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Fehler: {err}")
        exit(1)

# Datenbank erstellen
def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as err:
        print(f"Fehler beim Erstellen der Datenbank: {err}")
        exit(1)

# Tabellen erstellen
def create_tables(cnx):
    cursor = cnx.cursor()
    try:
        cursor.execute(f"USE {DB_NAME}")
    except mysql.connector.Error as err:
        print(f"Fehler: {err}")
        exit(1)

    for table_name, ddl in TABLES.items():
        try:
            print(f"Erstelle Tabelle {table_name}...")
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            print(f"Fehler beim Erstellen von Tabelle {table_name}: {err}")

    cursor.close()

# Hauptfunktion
def main():
    cnx = connect_to_database()
    cursor = cnx.cursor()

    try:
        create_database(cursor)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Datenbank {DB_NAME} existiert bereits.")
        else:
            print(f"Fehler: {err}")
            exit(1)

    create_tables(cnx)
    cnx.close()

if __name__ == "__main__":
    main()