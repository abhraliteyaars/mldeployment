import mysql.connector
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')




def write_data_db(price, area, bedrooms, bathrooms, stories,timestamp):

    #connect to the database
    mysqldb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    passwd=db_pass,
    database=db_name)

    #define cursor
    cursor = mysqldb.cursor()

    # price = 1000000
    # area = 2500
    # bedrooms = 4
    # bathrooms = 1
    # stories = 1
    # timestamp = datetime.datetime.now()

    #insert data into the table
    sql = "INSERT INTO apartment_price (price, area, bedrooms, bathrooms, stories,timestamp) VALUES (%s, %s, %s, %s, %s,%s)"
    val = (price, area, bedrooms, bathrooms, stories,timestamp)
    cursor.execute(sql, val)
    mysqldb.commit()

    print(cursor.rowcount, "record inserted.")
    #close the cursor and connection
    cursor.close()
    mysqldb.close()