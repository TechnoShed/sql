from datetime import datetime
import mysql.connector
from mysql.connector import Error

# Classes first script

# THIS WILL BE THE BASIS OF THE VEHICLE INVENTORY SYSTEM

# GLOBAL VARIABLES

serverhost = "192.168.1.201"
serveruser = "root"
serverpass = "TSD704153TSD"

class comment():
    def __init__(self, ID, REG, DateTime, User, Comment):
        self.id= ID
        self.reg= REG
        self.datetime= DateTime
        self.user =User
        self.comment= Comment
    def add(self):
        self.datetime = str(datetime.now())
        # self.user = "sys-commentor"
        mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="""INSERT INTO comments VALUES(%s ,%s ,%s, %s ,%s) """
            input_data = (self.id,self.reg,self.datetime,self.user,self.comment)
            mycursor.execute(command,input_data)
            mycursor.close()
            mydb.commit()
            mydb.close()
            return

class inspection():
    def __init__(self , ID, REG, Inspector, DateTime, Location, Mileage, Front_Image, OS_Image, NS_Image, Rear_Image, Dash_Alerts, Fuel_Level, Oil_Level, Coolant_Level, Brake_Fluid_Level, Steering_Fluid_Level, Screenwash_Level,Hoses,Belts,Tyre_Pressures,NSF_Tyre,OSF_Tyre,OSR_Tyre,NSR_Tyre,Front_Lights,Rear_Lights,Other_Lights,Windscreen_Clear,Horn,Seat_Belts,Wipers,Rear_Wipers,Hand_Brake,Med_Kit,OS_Doors,NS_Doors,Notes,Images,Attachments,PassFail,Filename,Site,AdBlue):
        self.id =ID
        self.reg=REG
        self.inspector=Inspector
        self.datetime=DateTime
        pass

class vehicle():
    def __init__(self,ID, REG, VIN, Make, Model, Year, Colour, Mileage, Type, Image, Inspector, DateTime_Updated, Status, Site):
        self.id=ID
        self.reg=REG
        self.vin=VIN
        self.make=Make
        self.model=Model
        self.year=Year
        self.colour=Colour
        self.mileage=Mileage
        self.type=Type
        self.image=Image
        self.inspector=Inspector
        self.updated=DateTime_Updated
        self.status=Status
        self.site=Site
    def updateMileage(self, mileage):
        self.inspector = "mileage-upd"
        print("MILEAGE-UPD    :"+self.colour+" "+self.make+" "+self.model+"("+self.reg+") from "+ str(self.mileage)+" to "+str(mileage))
        oldmileage = self.mileage
        self.mileage = mileage
        self.updated = datetime.now()
        mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="UPDATE vehicles SET mileage= '" + str(self.mileage) + "', DateTime_Updated= '" + str(self.updated) + "', Inspector= '"+self.inspector+"' WHERE reg='" + self.reg +"'"
            mycursor.execute(command)
            mycursor.close()
            mydb.commit()
            mydb.close()
            newcomment = comment("",self.reg,str(self.updated),"upd-mileage","Mileage Updated from "+str(oldmileage)+" to "+str(self.mileage))
            newcomment.add()
            return
    def writeback(self):
        self.updated = datetime.now()
        self.inspector = "veh-write"
        mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="""UPDATE vehicles SET VIN=%s, Make=%s, Model=%s, Year=%s, Color=%s, Mileage=%s,Type=%s,Image=%s,Inspector=%s,DateTime_Updated=%s,Status=%s, Site=%s WHERE reg=%s"""
            input_data = (self.vin,self.make,self.model,str(self.year),self.colour,str(self.mileage),self.type,self.image,self.inspector,str(self.updated),self.status,self.site,self.reg)
            mycursor.execute(command, input_data)
            mycursor.close()
            mydb.commit()
            mydb.close()
            newcomment = comment("",self.reg,str(self.updated),"veh-writeback","Record Updated")
            newcomment.add()
            print("DB:WRITEBACK   :"+self.colour+" "+self.make+" "+self.model+"("+self.reg+") with "+str(self.mileage)+" mls. Updated @ "+str(self.updated)+" by "+ self.inspector)
            return
    def getMileage(self):
        return self.mileage
    def getLastUpdate(self):
        return self.updated , self.inspector
    def createComment(self,text):
        updatetime = str(datetime.now())

        print("creating comment on "+self.colour+" "+ self.make+" "+self.model+"("+self.reg+") : "+str(text))
        newcomment = comment("",self.reg,str(updatetime),"veh-comment",text)
        newcomment.add()
        pass

def readVehicle(reg):
    mydb = mysql.connector.connect(host=serverhost,
                            user=serveruser,
                            database='inspections',
                            password=serverpass)
    mycursor = mydb.cursor()
    if mydb.is_connected():
        command ="SELECT * FROM vehicles WHERE reg='" + reg +"'"
        mycursor.execute(command)
        for x in mycursor :
            foundvehicle=vehicle(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13])
            print("DB:READ        :"+foundvehicle.colour+" "+foundvehicle.make+" "+foundvehicle.model+"("+foundvehicle.reg+") with "+str(foundvehicle.mileage)+" mls. Updated @ "+str(foundvehicle.updated)+" by "+ foundvehicle.inspector)
        mycursor.close()
        mydb.commit()
        mydb.close()
        return foundvehicle

van=readVehicle("GD18XOU")
#van.createComment("Fuck NIXON chfdhos he is mega bent")
#van.updateMileage(4000)
#van.colour="White"
#van.writeback()
