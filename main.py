import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
import tkinter as tk

serverhost = "technoshed.duckdns.org"
serveruser = "root"
serverpass = "TSD704153TSD"

def dfquerymysql(searchstr):
    query = searchstr
    print(query)
    mydb = create_engine("mysql+pymysql://{user}:{pw}@{server}/{db}"
                    .format(user=serveruser,
                            pw=serverpass,
                            server=serverhost,
                            db="inspections"))
    new_df1 =pd.read_sql_query(query, mydb)
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
def querydb(query):
    mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
    mycursor = mydb.cursor()
    if mydb.is_connected():
            #print("QUERYING with  "+query)
            mycursor.execute(query)
            data=mycursor.fetchone()
            mycursor.close()
            mydb.close()
            return data
def updatedb(query):
    mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
    mycursor = mydb.cursor()
    if mydb.is_connected():
            #print("UPDATING with  "+query)
            mycursor.execute(query)
            mycursor.close()
            mydb.commit()
            mydb.close()
            return

def getvehicledetails(reg):
    print("Retrieving details for "+ str(reg))
    
    detailquery = "SELECT * FROM inspections.vehicles WHERE REG='"+reg+"'"
    commentquery = "SELECT * FROM inspections.comments WHERE REG='"+reg+"'"
    inspectionquery = "SELECT * FROM inspections.inspections WHERE REG='"+reg+"'"

    details = dfquerymysql(detailquery)
    comments = dfquerymysql(commentquery)
    inspections =dfquerymysql(inspectionquery)
    #comments = comments['DateTime','User','Comment']
    return details , comments , inspections

def updatemileage(reg , mileage):
    query="UPDATE vehicles SET Mileage="+ str(mileage)+" WHERE REG='"+reg+"';"
    updatedb(query)
    return mileage

def getmileage(reg):
    query="SELECT mileage, reg FROM inspections.vehicles WHERE REG='"+reg+"'"
    mileage = querydb(query)[0]
    return mileage


    # print("\n\nVEHICLE DETAILS\n")
    # print(details)
    # print("\nEVENTS\n")
    # print(comments)
    # print("\nINSPECTIONS\n")
    # print(inspections)
    
print("TechnoShed Studios MYSQL Fleet Manager functions test\n\n")
# showmysql()
searchstr = "GD18XOZ"

mileage =getmileage(searchstr)
updatemileage(searchstr, 3000)
newmileage=getmileage(searchstr)
print(searchstr+" has a mile of "+str(mileage) +" and now has a mileage of" + str(newmileage))
#vehicledetails, vehiclecomments, vehicleinspections = getvehicledetails(searchstr)

# print(vehicledetails)
# print(vehiclecomments)
# print(vehicleinspections)


# root=tk.Tk()
# root.title("Vehicle Search")
# root.geometry('1024x800')

# # topframe = tk.LabelFrame(tframe, text="Information", borderwidth=2, relief="ridge")
# #     topframe.grid(row=0, column=0,columnspan=2, padx=5,pady=5)
# #     mainframe =tk.LabelFrame(tframe, text="Processed Data")
# #     mainframe.grid(row=1, column=0, padx=5, pady=5)
# #     rightframe= tk.LabelFrame(tframe, text="AML Email Data")
# #     rightframe.grid(row=1,column=1, padx=5, pady=5)



# topFrame = tk.LabelFrame(root, text="Search Box", borderwidth=5, relief="ridge", bg ="light blue")
# bottomFrame = tk.LabelFrame(root, text="Vehicle Details", borderwidth=5, relief="ridge", bg="light green")

# topFrame.pack()
# bottomFrame.pack()

# # define form

# searchLabel = tk.Label(topFrame, text="REGISTRATION")
# searchEntry = tk.Entry(topFrame, text="Enter Reg Here")
# searchButton = tk.Button(topFrame, text="SEARCH")

# details = tk.Text(bottomFrame,height=40, width=100)

# detailscroll = tk.Scrollbar(details)

# details = tk.Text(bottomFrame, height=40, width=100, padx=1, yscrollcommand=detailscroll.set, bg="light yellow", fg="black")
# details.pack(side = "left", fill=tk.Y)
# detailscroll.pack(side="right", fill=tk.Y)  
# detailscroll.config(command=details.yview)


# # pack form

# searchLabel.grid(row=0, column=0)
# searchEntry.grid(row=0, column=2)
# searchButton.grid(row=1,column=1)

# root.mainloop()
