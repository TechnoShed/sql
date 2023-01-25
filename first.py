# Script to connect to my SQL server and try and create a table
import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
# import pymysql

# Function to connect and open database

def showmysql():
    mydb = mysql.connector.connect(host='192.168.1.201',
                                 user='root',
                                 database='inspections',
                                 password='TSD704153TSD')
    mycursor = mydb.cursor()
    if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            record = mycursor.fetchone()
            print("You're connected to database: ", record)
            mycursor.execute("SHOW TABLES")

            for x in mycursor:
                print(x) 

            mycursor.close()
            mydb.close()
            print("COnnection closed")


# Load Inspections XL data into dataframes

#df_inspections = pd.read_excel('data.xlsx', sheet_name='Inspections')
#df_events = pd.read_excel('data.xlsx', sheet_name='Events')
#df_comments = pd.read_excel('data.xlsx', sheet_name='Comments')
#df_users = pd.read_excel('data.xlsx', sheet_name='Users')
#df_vehicles = pd.read_excel('data.xlsx', sheet_name='Vehicles')
#print(df_inspections)
#print(df_vehicles)
#print(df_events)
#print(df_events)
#print(df_users)

#mydb = mysql.connector.connect(host='192.168.1.201',
#                                 user='root',
#                                 database='inspections',
#                                 password='TSD704153TSD')
 # create sqlalchemy engine
mydb = create_engine("mysql+pymysql://{user}:{pw}@192.168.1.201/{db}"
                   .format(user="root",
                           pw="TSD704153TSD",
                           db="inspections"))
   
#tableName = "inspections"
try:

   print("running queries...")
   #frame           = df_inspections.to_sql(tableName, mydb, if_exists='fail');

except ValueError as vx:#

    print(vx)

except Exception as ex:

    print(ex)

else:

    print("done");
    #print("Table %s created successfully."%tableName);

finally:
    print("ended")

showmysql()

new_df =pd.read_sql('SELECT * FROM inspections WHERE Inspector="upykey@gmail.com"', mydb)

print(new_df)