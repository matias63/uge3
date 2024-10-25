import pandas as pd
import mysql.connector
import base64
import pyodbc 

def main():
    encoded_password = obscufate_data()
    database_connect(encoded_password)

    # df = pd.read_csv('data.csv')
    # print(df)


def obscufate_data():
    print(base64.b64encode("TYXpopKBR67()".encode("utf-8")))
    encoded_password = base64.b64encode("password".encode("utf-8"))
    print(base64.b64decode(encoded_password).decode("utf-8"))
    return encoded_password

def database_connect(encoded_password):
    
    # # Connect to server
    # cnx = mysql.connector.connect(
    #     host="localhost",
    #     port=3306,
    #     user="matias",
    #     password=f"{encoded_password}")

    # # Get a cursor
    # cur = cnx.cursor()

    # # Execute a query
    # cur.execute('SELECT OrderID FROM Orders WHERE ShipRegion is NULL and  ShipCountry = "Germany" and Freight >= 100 and EmployeeID = 1 and YEAR(OrderDate) = 1996;')
    # # cur.execute("SELECT CURDATE()")

    # # Fetch one result
    # row = cur.fetchone()
    # print("Current date is: {0}".format(row[0]))

    # # Close connection
    # cnx.close()

    SQL_DRIVER = "{MySQL ODBC 8.0 ANSI Driver}"
    SQL_SERVER = "localhost"
    SQL_USERNAME = "matias"
    SQL_PASSWORD = "Test1234"

    # Create connection to MySQL database
    cnxn = pyodbc.connect(
        f"DRIVER={SQL_DRIVER};SERVER={SQL_SERVER};UID={SQL_USERNAME};PWD={SQL_PASSWORD}"
    )

    # Create a cursor from the connection
    cursor = cnxn.cursor()
    cursor.execute("USE northwind;")
    cursor.execute('SELECT OrderID FROM Orders WHERE ShipRegion is NULL and  ShipCountry = "Germany" and Freight >= 100 and EmployeeID = 1 and YEAR(OrderDate) = 1996;')
    rows = cursor.fetchall()
    print(rows)
    cursor.description
    breakpoint()

    cursor.close()

if __name__ == "__main__":
    main()
