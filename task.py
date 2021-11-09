import pandas as pd
empdata = pd.read_csv('code_challenge.csv', index_col=False, delimiter = ';',)
# print(empdata.head())
import mysql.connector as msql
from mysql.connector import Error

mydb = msql.connect(
  host="localhost",
  user="root",
#   password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS test_db")

try:
    conn = msql.connect(host='localhost', user='root', password='',
        database='test_db',
    )#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS test_db;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute('''CREATE TABLE IF NOT EXISTS test_table(
            Created_Date DATE, 
            Ad_Unit_Name VARCHAR(255), 
            Ad_Unit_ID INT NOT NULL PRIMARY KEY, 
            Typetag INT, 
            Revenue_Source VARCHAR(255), 
            Market VARCHAR(255), 
            Queries BIGINT(255), 
            Clicks INT, 
            Impressions INT, 
            Page_Rpm INT, 
            Impression_Rpm INT, 
            True_Revenue VARCHAR(255), 
            Coverage VARCHAR(255), 
            Ctr VARCHAR(20))''')
        
        print("Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO test_db.test_table VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)