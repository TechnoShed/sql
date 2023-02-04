from datetime import datetime
import mysql.connector
from mysql.connector import Error

# Classes first script

# THIS WILL BE THE BASIS OF THE VEHICLE INVENTORY SYSTEM

# GLOBAL VARIABLES

#serverhost = "192.168.1.201"
serverhost = "technoshed.duckdns.org"
serveruser = "root"
serverpass = "TSD704153TSD"

class comment():
    def __init__(self, REG, DateTime, User, Comment):
        self.reg= REG
        self.datetime= DateTime
        self.user =User
        self.comment= Comment
    def add(self):
        self.datetime = str(datetime.now())
        #self.user = "sys-comment"
        mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="""INSERT INTO comments VALUES(%s ,%s ,%s, %s) """
            input_data = (self.reg,self.datetime,self.user,self.comment)
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
        self.location=Location
        self.Mileage=Mileage
        self.frimage=Front_Image
        self.osimage=OS_Image
        self.nsimage=NS_Image
        self.rrimage=Rear_Image
        self.dash=Dash_Alerts
        self.fuel=Fuel_Level
        self.oil=Oil_Level
        self.coolant=Coolant_Level
        self.brakef=Brake_Fluid_Level
        self.steeringf=Steering_Fluid_Level
        self.screenwash=Screenwash_Level
        self.hoses=Hoses
        self.belts=Belts
        self.pressures=Tyre_Pressures
        self.nsftyre=NSF_Tyre
        self.osftyre=OSF_Tyre
        self.osrtyre=OSR_Tyre
        self.nsrtyre=NSR_Tyre
        self.frlights=Front_Lights
        self.rrlights=Rear_Lights
        self.olights=Other_Lights
        self.windscreen=Windscreen_Clear
        self.horn=Horn
        self.seatbelts=Seat_Belts
        self.fwipers=Wipers
        self.rwipers=Rear_Wipers
        self.hbrake=Hand_Brake
        self.medkit=Med_Kit
        self.osdoors=OS_Doors
        self.nsdoors=NS_Doors
        self.notes=Notes
        self.image=Images
        self.attachments=Attachments
        self.passfail=PassFail
        self.filename=Filename
        self.site=Site
        self.adblue=AdBlue

    def add(self):
        self.datetime = str(datetime.now())
        self.inspector = "sys-ins-added"
        mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="""INSERT INTO inspections VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            
            input_data= (self.id,
            self.reg,
            self.inspector,
            str(self.datetime),
            self.location,
            str(self.Mileage),
            self.frimage,
            self.osimage,
            self.nsimage,
            self.rrimage,
            self.dash,
            self.fuel,
            self.oil,
            self.coolant,
            self.brakef,
            self.steeringf,
            self.screenwash,
            self.hoses,
            self.belts,
            self.pressures,
            self.nsftyre,
            self.osftyre,
            self.osrtyre,
            self.nsrtyre,
            self.frlights,
            self.rrlights,
            self.olights,
            self.windscreen,
            self.horn,
            self.seatbelts,
            self.fwipers,
            self.rwipers,
            self.hbrake,
            self.medkit,
            self.osdoors,
            self.nsdoors,
            self.notes,
            self.image,
            self.attachments,
            self.passfail,
            self.filename,
            self.site,
            self.adblue)

            input_data = (self.vin,self.make,self.model,str(self.year),self.colour,str(self.mileage),self.type,self.image,self.inspector,str(self.updated),self.status,self.site)
            mycursor.execute(command, input_data)
            mycursor.close()
            mydb.commit()
            mydb.close()
            newcomment = comment("",self.reg,str(self.updated),"sys-veh","Record Created")
            newcomment.add()
            print("DB:CREATE   :"+self.colour+" "+self.make+" "+self.model+"("+self.reg+") with "+str(self.mileage)+" mls. created @ "+str(self.updated)+" by "+ self.inspector)
            return           

      
class vehicle():
    def __init__(self,ID, REG, VIN, Make, Model, Year, Colour, Mileage, Type, Image, Inspector, DateTime_Updated, Status, Site):
        self.id=ID
        self.reg=REG.upper()
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
    def add(self):
        self.datetime = str(datetime.now())
        # self.user = "sys-veh-added"
        mydb = mysql.connector.connect(host=serverhost,
                                 user=serveruser,
                                 database='inspections',
                                 password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="""INSERT INTO vehicles VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            input_data = (self.vin,self.make,self.model,str(self.year),self.colour,str(self.mileage),self.type,self.image,self.inspector,str(self.updated),self.status,self.site)
            mycursor.execute(command, input_data)
            mycursor.close()
            mydb.commit()
            mydb.close()
            newcomment = comment("",self.reg,str(self.updated),"sys-veh","Record Created")
            newcomment.add()
            print("DB:CREATE   :"+self.colour+" "+self.make+" "+self.model+"("+self.reg+") with "+str(self.mileage)+" mls. created @ "+str(self.updated)+" by "+ self.inspector)
            return          
    def updateMileage(self, mileage):
        self.inspector = "sys-upd-mileage"
        self.read()
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
            newcomment = comment(self.reg,str(self.updated),"sys-upd-mileage","Mileage Updated from "+str(oldmileage)+" to "+str(self.mileage))
            newcomment.add()
            return
    def writeback(self):
        self.updated = datetime.now()
        #self.inspector = "veh-write"
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
            # newcomment = comment("",self.reg,str(self.updated),"veh-writeback","Record Updated")
            # newcomment.add()
            print("DB:WRITEBACK   :"+self.colour+" "+self.make+" "+self.model+"("+self.reg+") with "+str(self.mileage)+" mls. Updated @ "+str(self.updated)+" by "+ self.inspector)
            return
    def getMileage(self):
        return self.mileage
    def getLastUpdate(self):
        return self.updated , self.inspector
    def createComment(self,text):
        updatetime = str(datetime.now())
        print("creating comment on "+self.colour+" "+ self.make+" "+self.model+"("+self.reg+") : "+str(text))
        newcomment = comment(self.reg,str(updatetime),"veh-comment",text)
        newcomment.add()
        pass
    def getComments(self):
        mydb = mysql.connector.connect(host=serverhost,
                            user=serveruser,
                            database='inspections',
                            password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="SELECT datetime,user,comment FROM comments WHERE reg='" + self.reg +"' ORDER BY datetime DESC"
            mycursor.execute(command)
            counter=0
            output = ""

            for x in mycursor :
                # self.datetime = x[1]
                # self.user = x[2]
                # self.comment = x[3]
                output = output + str(counter+1)+" - "+str(x[0])+" by "+str(x[1])+"\n   "+str(x[2])+"\n\n"
                counter = counter +1
            print("Retreived "+str(counter)+" Comments on "+self.reg.upper())
            mycursor.close()
            mydb.commit()
            mydb.close()
        return output
    def read(self):
        mydb = mysql.connector.connect(host=serverhost,
                            user=serveruser,
                            database='inspections',
                            password=serverpass)
        mycursor = mydb.cursor()
        if mydb.is_connected():
            command ="SELECT * FROM vehicles WHERE reg='" + self.reg +"'"
            mycursor.execute(command)
            for x in mycursor :
                self.vin = x[2]
                self.make = x[3]
                self.model = x[4]
                self.year = x[5]
                self.colour = x[6]
                self.mileage = x[7]
                self.type = x[8]
                self.image = x[9]
                self.inspector = x[10]
                self.updated = x[11]
                self.status = x[12]
                self.site = x[13]
                print("DB:VEH-READ    :"+self.colour+" "+self.make+" "+self.model+"("+self.reg+") with "+str(self.mileage)+" mls. Updated @ "+str(self.updated)+" by "+ self.inspector)
            mycursor.close()
            mydb.commit()
            mydb.close()
        return
    def startinspection(self):
        updatetime = str(datetime.now())
        self.createComment("Started Inspection at "+updatetime)
        inspect=inspection("",self.reg,"", updatetime ,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",)
        return inspect


van = vehicle("","FD22VSC","","","","","","","","","","","","")
#print("updating mileage on VAN reg "+van.reg)
#van.read()
    
#van.createComment("Messing with this one")

#van.mileage=van.mileage+1000
#van.colour="White"
#van.updateMileage(3048)
#van.writeback()
#van.createComment("YOu on the other hand, mouth and bumhole, LOVE cock")

# myinspection=van.startinspection()
# print("REG : "+van.reg)
# print("INSPECTION : "+myinspection.reg+"\nCreated : "+str(myinspection.datetime))


# TKinter portion GUI

# Setup root window properties


root=tk.Tk()
root.title("TechnoShed Studios - Fleet Vehicle Database")
#root.geometry('1024x600')
foundvan = vehicle("","","","","","","","","","","","","","")
    
# define search frame

searchFrame = tk.LabelFrame(root, text="Search Box", borderwidth=5, relief="ridge", bg ="light blue")
searchLabel = tk.Label(searchFrame, text="REG")
searchEntry = tk.Entry(searchFrame)

# define vehicle and database frame
databaseFrame = tk.LabelFrame(root, text="Database Results "+str(searchEntry.get()), borderwidth=5, relief="ridge", bg="light green")
vehicleFrame = tk.LabelFrame(root, text="Vehicle Details", borderwidth=5, relief="ridge", bg="light blue")

# define comment frame

commentFrame= tk.LabelFrame(root, text="Comments on "+str(foundvan.reg), borderwidth=5, relief="ridge", bg="light blue",fg="black")
commentBox= tk.Text(commentFrame,  height=11, width=37, pady=5,padx=5, bg="light yellow", fg="black")

# place frames with grid()
databaseFrame.grid(row=0,column=0,columnspan=2,rowspan=7)
searchFrame.grid(row=0,column=2,columnspan=2)
vehicleFrame.grid(row=1,column=2,columnspan=2,rowspan=2)
commentFrame.grid(row=4,column=2,columnspan=2,rowspan=2)

# place comments qidgets in commentFrame

commentBox.grid(row=0, column=0, columnspan=2)


# define vehicle details frame

regLabel = tk.Label(vehicleFrame, width=20, text="Registration")
regEntry = tk.Entry(vehicleFrame, width=25)

mileageLabel = tk.Label(vehicleFrame, width=20, text="Mileage")
mileageEntry = tk.Entry(vehicleFrame, width=25,)
makeLabel = tk.Label(vehicleFrame, width=20, text="Make")
makeEntry = tk.Entry(vehicleFrame, width=25)
modelLabel = tk.Label(vehicleFrame, width=20, text="Model")
modelEntry = tk.Entry(vehicleFrame, width=25)
colourLabel = tk.Label(vehicleFrame, width=20, text="Colour")
colourEntry = tk.Entry(vehicleFrame, width=25)
vinLabel = tk.Label(vehicleFrame, width=20, text="VIN")
vinEntry = tk.Entry(vehicleFrame, width=25)
typeLabel = tk.Label(vehicleFrame, width=20, text="Type")
typeEntry = tk.Entry(vehicleFrame, width=25)
statusLabel = tk.Label(vehicleFrame, width=20, text="Status")
statusEntry = tk.Entry(vehicleFrame, width=25)
siteLabel = tk.Label(vehicleFrame, width=20, text="Site")
siteEntry = tk.Entry(vehicleFrame, width=25)
inspectorLabel = tk.Label(vehicleFrame, width=20, text="Updated by")
inspectorEntry = tk.Entry(vehicleFrame, width=25)
datetimeLabel = tk.Label(vehicleFrame, width=20, text="Updated at")
datetimeEntry = tk.Entry(vehicleFrame, width=25)
cancelButton = tk.Button(vehicleFrame,width=15, padx=5, pady=5, text="CANCEL")
acceptButton = tk.Button(vehicleFrame,width=15,padx=5, pady=5, text="SUBMIT")


regLabel.grid(row=0, column=0)
regEntry.grid(row=0, column=2,padx=2,pady=2)

mileageLabel.grid(row=2, column=0)
mileageEntry.grid(row=2, column=2,padx=2,pady=2)
makeLabel.grid(row=3, column=0)
makeEntry.grid(row=3, column=2)
modelLabel.grid(row=4, column=0)
modelEntry.grid(row=4, column=2)
colourLabel.grid(row=5, column=0)
colourEntry.grid(row=5, column=2)
vinLabel.grid(row=6, column=0)
vinEntry.grid(row=6, column=2)
typeLabel.grid(row=7, column=0)
typeEntry.grid(row=7, column=2)
statusLabel.grid(row=8, column=0)
statusEntry.grid(row=8, column=2)
siteLabel.grid(row=9, column=0)
siteEntry.grid(row=9, column=2)
inspectorLabel.grid(row=10, column=0)
inspectorEntry.grid(row=10, column=2)
datetimeLabel.grid(row=11, column=0)
datetimeEntry.grid(row=11, column=2)
cancelButton.grid(row=12, column=0)
acceptButton.grid(row=12, column=2)

def updateVehiclePane(veh):
    #   Update Vehicle Details form with loaded record
    #print("Update vehicle pane: with vehicle "+str(veh.reg)) # output for debugging
    regEntry.config(text=veh.reg.upper())
    regEntry.delete(0,"end")
    makeEntry.delete(0,"end")
    modelEntry.delete(0,"end")
    colourEntry.delete(0,"end")
    vinEntry.delete(0,"end")
    mileageEntry.delete(0,"end")
    typeEntry.delete(0,"end")
    statusEntry.delete(0,"end")
    siteEntry.delete(0,"end")
    inspectorEntry.delete(0,"end")
    datetimeEntry.delete(0,"end")
    regEntry.insert(0,veh.reg)
    makeEntry.insert(0,veh.make)
    modelEntry.insert(0,veh.model)
    colourEntry.insert(0,veh.colour)
    vinEntry.insert(0,str(veh.vin))
    mileageEntry.insert(0,str(veh.mileage))
    typeEntry.insert(0,veh.type)
    statusEntry.insert(0,veh.status)
    siteEntry.insert(0,veh.site)
    inspectorEntry.insert(0,veh.inspector)
    datetimeEntry.insert(0,veh.updated)
    return
  
def searchvehicle():
    reg = str(searchEntry.get())
    print("Searching for "+reg)
    details.delete("1.0", "end")
    global foundvan
    foundvan = vehicle("",reg,"","","","","","","","","","","","")
    foundvan.read()
    if foundvan.make !="":
        databaseFrame.configure( text="Database Results for "+str(foundvan.reg))
        output = "Comments for "+foundvan.reg
        details.delete("1.0","end")
        details.insert("1.0", output+"\n")
        updateVehiclePane(foundvan)
        outputcomments = foundvan.getComments()  
        details.insert("6.0", "\n"+ outputcomments+"\n")
    else:
        databaseFrame.configure( text="NO RESULTS for "+str(reg))
        output="VEHICLE "+reg+" NOT FOUND"
        details.delete("1.0","end")
        details.insert("1.0", output)
    return foundvan

def updatemile():
    foundvan.updateMileage(mileageEntry.get()) 

def addcomment():
    foundvan.createComment(commentBox.get("1.0","end"))
    commentBox.delete("1.0","end")
    pass

searchButton = tk.Button(searchFrame, padx=5, pady=5, text="SEARCH",command=searchvehicle)
commentButton =tk.Button(commentFrame, padx=5, pady=5, text="SUBMIT Comment", command=addcomment)
commentButton.grid(row=1,column=1, columnspan=2)

details = tk.Text(databaseFrame, height=37, width=60, pady=5,padx=5, bg="light yellow", fg="black")
details.grid(row=0, column=0)


# pack form

searchLabel.grid(row=0, column=0, padx=5, pady=5)
searchEntry.grid(row=0, column=2, padx=5, pady=5)
searchButton.grid(row=1,column=2, padx=5, pady=5)
#
root.bind('<Return>', (lambda event: searchvehicle()))
mileageEntry.bind('<Return>',(lambda event: updatemile()))
commentBox.bind('<Return>',(lambda event:addcomment()))

root.mainloop()
