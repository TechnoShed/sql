# Script to connect to my SQL server and try and create a table
import pandas as pd
import mysql.connector
from mysql.connector import Error

# Function to connect and open database

def showmysql():
    mydb = mysql.connector.connect(host='192.168.1.201',
                                 user='root',
                                 database='inspections',
                                 password='TSD704153TSD')
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

  #  for x in mycursor:
  #  print(x) 


# Load Inspections XL data into dataframes

df_inspections = pd.read_excel('data.xlsx', sheet_name='Inspections')
df_events = pd.read_excel('data.xlsx', sheet_name='Events')
df_comments = pd.read_excel('data.xlsx', sheet_name='Comments')
df_users = pd.read_excel('data.xlsx', sheet_name='Users')
df_vehicles = pd.read_excel('data.xlsx', sheet_name='Vehicles')
print(df_inspections)
print(df_vehicles)
print(df_events)
print(df_events)
print(df_users)
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")