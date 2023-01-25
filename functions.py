import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine

def querymysql(tablename,field, searchstr):
    query = "SELECT * FROM " + tablename + " WHERE "+field +"='" + searchstr + "'"
    print(query)
    mydb = create_engine("mysql+pymysql://{user}:{pw}@192.168.1.201/{db}"
                    .format(user="root",
                            pw="TSD704153TSD",
                            db="inspections"))
    new_df1 =pd.read_sql_query(query, mydb, index_col="REG")
    numresults = len(new_df1.index)
    return numresults, new_df1

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

print("TechnoShed Studios MYSQL Fleet Manager functions test")
showmysql()
df=querymysql("vehicles","Type","'*'")[1]
print(df)