import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
import tkinter as tk

serverhost = "192.168.1.201"
serveruser = "root"
serverpass = "TSD704153TSD"

def querymysql(tablename,field, searchstr):
    query = "SELECT * FROM " + tablename + " WHERE "+field + searchstr
    print(query)
    mydb = create_engine("mysql+pymysql://{user}:{pw}@{server}/{db}"
                    .format(user=serveruser,
                            pw=serverpass,
                            server=serverhost,
                            db="inspections"))
    new_df1 =pd.read_sql_query(query, mydb, index_col="REG")
    return new_df1

def showmysql():
    mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
    mycursor = mydb.cursor()
    if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            #mycursor.execute("SHOW TABLES")
            #for x in mycursor:
            #    print(x) 
            mycursor.close()
            mydb.close()

def showtabledetails(tablename):
    mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
    mycursor = mydb.cursor()
    if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            print("\nDESCRIBEing table : " + tablename +"\n")
            command = "DESCRIBE " + tablename
            mycursor.execute(command)
            for x in mycursor:
                print("Field: " +x[0]+"\t\t"+x[1]) 
            mycursor.close()
            mydb.close()

def copymysql( df,tablename ):
    mydb = create_engine("mysql+pymysql://{user}:{pw}@{server}/{db}"
                    .format(user=serveruser,
                            pw=serverpass,
                            server=serverhost,
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
    mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
    query = "SELECT * FROM " + tablename
    if mydb.is_connected():
            new_df =pd.read_sql(query, mydb)
            mydb.close()
    return new_df

def getvehicledetails(reg):
    print("Retrieving details for "+ str(reg))
    regstr = "='" + reg + "'"
    details = querymysql("vehicles","REG",regstr)
    comments = querymysql("comments","REG",regstr)
    inspections =querymysql("inspections","REG",regstr)
    # comments = comments['DateTime','User','Comment']


    # print("\n\nVEHICLE DETAILS\n")
    # print(details)
    # print("\nEVENTS\n")
    # print(comments)
    # print("\nINSPECTIONS\n")
    # print(inspections)
    return details , comments , inspections


print("TechnoShed Studios MYSQL Fleet Manager functions test\n\n")
showmysql()
result = getvehicledetails("CU67VXH")

vehdetails = result[0]
vehcomments = result[1]
vehinspections = result[2]

root=tk.Tk()
root.title("Vehicle Search")
root.geometry('1024x800')

topFrame = tk.Frame(root, borderwidth=5, bg ="light blue")
bottomFrame = tk.Frame(root, borderwidth=5, bg="light green")

detailsFrame = tk.Frame(bottomFrame ,borderwidth=5, bg="light grey")
commentsFrame = tk.Frame(bottomFrame ,borderwidth=5, bg="light grey")
inspectionsFrame = tk.Frame(bottomFrame ,borderwidth=5, bg="light grey")

topFrame.pack()
bottomFrame.pack()
detailsFrame.grid(row=0,column=0)
commentsFrame.grid(row=1,column=0)
inspectionsFrame.grid(row=2,column=0)


# define form

searchLabel = tk.Label(topFrame, text="REGISTRATION")
searchEntry = tk.Entry(topFrame, text="Enter Reg Here")
searchButton = tk.Button(topFrame, text="SEARCH")

resultReg = tk.Label(detailsFrame, text="Vehicle")


resultBox = tk.Text(bottomFrame,height=40, width=100)

# pack form

searchLabel.grid(row=0, column=0)
searchEntry.grid(row=0, column=2)
searchButton.grid(row=1,column=1)


resultReg.grid(row=0, column=0)
resultBox.grid(row=2, column=0)
root.mainloop()
# showtabledetails("vehicles")
# showtabledetails("comments")
