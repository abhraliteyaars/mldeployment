import psycopg2
#import mysql.connector
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

def write_data_db(price, area, bedrooms, bathrooms, stories,timestamp):

    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
  
    #define cursor
    cursor = conn.cursor()

    #insert data into the table
    sql = "INSERT INTO price_predictor(price, area, bedrooms, bathrooms, stories,timestamp) VALUES (%s, %s, %s, %s, %s,%s)"
    val = (price, area, bedrooms, bathrooms, stories,timestamp)
    cursor.execute(sql, val)
    conn.commit()

    print(cursor.rowcount, "record inserted.")
    #close the cursor and connection
    cursor.close()