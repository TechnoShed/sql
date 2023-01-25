# Script to connect to my SQL server and try and create a table
import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
# import pymysql

def dropmysql(tablename):
    mydb = mysql.connector.connect(host='192.168.1.201',
                                 user='root',
                                 database='inspections',
                                 password='TSD704153TSD')
    mycursor = mydb.cursor()
    if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            mycursor.execute("DROP TABLE " +tablename)
            for x in mycursor:
                print(x) 
            mycursor.close()
            mydb.close()
            print("COnnection closed")

def showmysql():
    mydb = mysql.connector.connect(host='192.168.1.201',
                                 user='root',
                                 database='inspections',
                                 password='TSD704153TSD')
    mycursor = mydb.cursor()
    if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            mycursor.execute("SHOW TABLES")
            for x in mycursor:
                print(x) 
            mycursor.close()
            mydb.close()
            print("COnnection closed")

def copymysql( df,tablename ):
    mydb = create_engine("mysql+pymysql://{user}:{pw}@192.168.1.201/{db}"
                    .format(user="root",
                            pw="TSD704153TSD",
                            db="inspections"))
    try:
        frame           = df.to_sql(tablename, mydb, if_exists='fail', index=False);
    except ValueError as vx:#
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("done");
        print("Table %s created successfully."%tablename);

    finally:
        print("ended")

def showtable(tablename):
    mydb = mysql.connector.connect(host='192.168.1.201',
                                 user='root',
                                 database='inspections',
                                 password='TSD704153TSD')
    query = "SELECT * FROM " + tablename
    if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            new_df =pd.read_sql(query, mydb)
            print(new_df)
            mydb.close()
            print("COnnection closed")

def querymysql(tablename,field, searchstr):
    query = "SELECT * FROM " + tablename + " WHERE "+field +"='" + searchstr + "'"
    print(query)
    mydb = create_engine("mysql+pymysql://{user}:{pw}@192.168.1.201/{db}"
                    .format(user="root",
                            pw="TSD704153TSD",
                            db="inspections"))
    new_df1 =pd.read_sql_query(query, mydb)
    numresults = len(new_df1.index)
    print(numresults)
    return numresults, new_df1


# Load Inspections XL data into dataframes
# df_inspections = pd.read_excel('data.xlsx', sheet_name='Inspections')
# df_events = pd.read_excel('data.xlsx', sheet_name='Events')
# df_comments = pd.read_excel('data.xlsx', sheet_name='Comments')
# df_users = pd.read_excel('data.xlsx', sheet_name='Users')
# df_vehicles = pd.read_excel('data.xlsx', sheet_name='Vehicles')

#copymysql(df_comments, "comments")
#showmysql()
#showtable("comments")
result_df=querymysql("comments","REG","FD22VSK")
print(result_df )
result_df=querymysql("vehicles","REG","FD22VSK")
print(result_df)