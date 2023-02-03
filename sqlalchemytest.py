# NEW script using SQLalchemy to interface with SQL database instead of sql.connector and raw SQL 

# THIS WILL BE THE BASIS OF THE VEHICLE INVENTORY SYSTEM

from datetime import datetime
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Identity
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import random

Base = declarative_base()

# GLOBAL VARIABLES

serverhost = "192.168.1.201"
serverdb = "inspectionDB"
connectionstring = "mysql+pymysql://root:TSD704153TSD@"+str(serverhost)+"/"+str(serverdb)

class Vehicle(Base):
    __tablename__ = "vehicles"

    reg = Column("reg", String(7), primary_key=True)
    make = Column("make",String(15))
    model = Column("model",String(15))
    colour = Column("colour",String(10))
    mileage = Column("mileage",Integer)
    year = Column("year",Integer)
    status = Column("status", String(4))
    site = Column("site",String(10))
    updatedby = Column("updatedby", String(20))
    updatedon = Column("updatedon",String(26))
    def __init__(self, reg, make, model, colour, mileage, year, status, site, updatedby, updatedon):
        self.reg = reg
        self.make = make
        self.model = model
        self.colour = colour
        self.mileage = mileage
        self.year = year
        self.status = status
        self.site = site
        self.updatedby = updatedby
        self.updatedon = updatedon
    def __repr__(self):
        return f"({self.reg}) {self.year} {self.colour} {self.make} {self.model} with Mileage {self.mileage} at Status {self.status} at {self.site} Last updated ({self.updatedby} on {self.updatedon})"
    def updateMileage(self, newmileage):
        timenow = str(datetime.now())
        print("MILEAGE UPDATE: on "+foundvan.reg+" from "+str(foundvan.mileage)+" to "+str(newmileage))
        mileagecomment = Comment(random.randint(0,999999), "Mileage Updated from "+str(foundvan.mileage)+" to "+str(newmileage),"MILEAGE UPD",timenow,foundvan.reg)
        session.add(mileagecomment)
        foundvan.mileage = newmileage
        session.commit()
        print("MILEAGE UPDATED")


class Comment(Base):
    __tablename__ = "comments"

    commentid = Column("commentid", Integer, Identity(start=1000,cycle=True),primary_key=True,)
    comment = Column("comment",String(128))
    commentby = Column("commentby",String(20))
    commenton = Column("commenton",String(26))
    reg = Column(String(7), ForeignKey(Vehicle.reg))
    
    def __init__(self, commentid, comment, commentby, commenton, reg):
        self.commentid = commentid
        self.reg = reg
        self.comment = comment
        self.commentby = commentby
        self.commenton = commenton
    def __repr__(self):
        return f("({self.commentid}) on {self.reg} at {self.updatedon} by {self.updatedby} :\t{self.comment}")

def makeconnection(): # Make connection to DB and RETURN the session
    print("DB:            CONNECTING...")
    engine= create_engine(str(connectionstring))
    print("DB:            CONECTED - Binding to engine")
    Base.metadata.create_all(bind=engine)
    print("SESSION:       CREATING SESSION")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def loadvehicle(reg): # takes GLOBAL session from makeconnection() and loads vehicle from DB into a Vehicle object
    vehicle = session.query(Vehicle).filter(Vehicle.reg == reg).first()
    if not vehicle:
        print("QUERY:         NO RESULTS FOUND")
    # else:
    #     print("DB:            LOADED reg "+ vehicle.reg)
    return vehicle

def savechanges(reason):
    global session
    present = str(datetime.now())
    print("SESSION:       COMMIT at "+str(present))
    foundvan.updatedon = present
    foundvan.updatedby = reason
    session.commit()

updatingreg = "XX11XXX"

timenow = str(datetime.now())

session = makeconnection()
#van = Vehicle(updatingreg,"TechnoShed","EV-01","Grey",4,2023,"TEST","Grimsby","DEV TEAM",timenow)
#session.add(van)
#savechanges()

foundvan = loadvehicle(updatingreg)
if not foundvan:
    print("ERROR LD REC:  Vehicle "+updatingreg+" NOT FOUND")
else:
    print("LD REC:        Found van "+foundvan.reg+" with mileage : "+str(foundvan.mileage))


foundvan.updateMileage(foundvan.mileage+666)


# commentnum = 18
# firstcomment = Comment(random.randint(0,999999),"Bog licking","Gonzo",timenow,updatingreg)
# session.add(firstcomment)
# savechanges()
#

# TKinter portion GUI

# Setup root window properties


# root=tk.Tk()
# root.title("TechnoShed Studios - Fleet Vehicle Database")
# #root.geometry('1024x600')
# foundvan = vehicle("","","","","","","","","","","","","","")
    
# # define search frame

# searchFrame = tk.LabelFrame(root, text="Search Box", borderwidth=5, relief="ridge", bg ="light blue")
# searchLabel = tk.Label(searchFrame, text="REG")
# searchEntry = tk.Entry(searchFrame)

# # define vehicle and database frame
# databaseFrame = tk.LabelFrame(root, text="Database Results "+str(searchEntry.get()), borderwidth=5, relief="ridge", bg="light green")
# vehicleFrame = tk.LabelFrame(root, text="Vehicle Details", borderwidth=5, relief="ridge", bg="light blue")

# # define comment frame

# commentFrame= tk.LabelFrame(root, text="Comments on "+str(foundvan.reg), borderwidth=5, relief="ridge", bg="light blue",fg="black")
# commentBox= tk.Text(commentFrame,  height=11, width=37, pady=5,padx=5, bg="light yellow", fg="black")

# # place frames with grid()
# databaseFrame.grid(row=0,column=0,columnspan=2,rowspan=7)
# searchFrame.grid(row=0,column=2,columnspan=2)
# vehicleFrame.grid(row=1,column=2,columnspan=2,rowspan=2)
# commentFrame.grid(row=4,column=2,columnspan=2,rowspan=2)

# # place comments qidgets in commentFrame

# commentBox.grid(row=0, column=0, columnspan=2)


# # define vehicle details frame

# regLabel = tk.Label(vehicleFrame, width=20, text="Registration")
# regEntry = tk.Entry(vehicleFrame, width=25)

# mileageLabel = tk.Label(vehicleFrame, width=20, text="Mileage")
# mileageEntry = tk.Entry(vehicleFrame, width=25,)
# makeLabel = tk.Label(vehicleFrame, width=20, text="Make")
# makeEntry = tk.Entry(vehicleFrame, width=25)
# modelLabel = tk.Label(vehicleFrame, width=20, text="Model")
# modelEntry = tk.Entry(vehicleFrame, width=25)
# colourLabel = tk.Label(vehicleFrame, width=20, text="Colour")
# colourEntry = tk.Entry(vehicleFrame, width=25)
# vinLabel = tk.Label(vehicleFrame, width=20, text="VIN")
# vinEntry = tk.Entry(vehicleFrame, width=25)
# typeLabel = tk.Label(vehicleFrame, width=20, text="Type")
# typeEntry = tk.Entry(vehicleFrame, width=25)
# statusLabel = tk.Label(vehicleFrame, width=20, text="Status")
# statusEntry = tk.Entry(vehicleFrame, width=25)
# siteLabel = tk.Label(vehicleFrame, width=20, text="Site")
# siteEntry = tk.Entry(vehicleFrame, width=25)
# inspectorLabel = tk.Label(vehicleFrame, width=20, text="Updated by")
# inspectorEntry = tk.Entry(vehicleFrame, width=25)
# datetimeLabel = tk.Label(vehicleFrame, width=20, text="Updated at")
# datetimeEntry = tk.Entry(vehicleFrame, width=25)
# cancelButton = tk.Button(vehicleFrame,width=15, padx=5, pady=5, text="CANCEL")
# acceptButton = tk.Button(vehicleFrame,width=15,padx=5, pady=5, text="SUBMIT")


# regLabel.grid(row=0, column=0)
# regEntry.grid(row=0, column=2,padx=2,pady=2)

# mileageLabel.grid(row=2, column=0)
# mileageEntry.grid(row=2, column=2,padx=2,pady=2)
# makeLabel.grid(row=3, column=0)
# makeEntry.grid(row=3, column=2)
# modelLabel.grid(row=4, column=0)
# modelEntry.grid(row=4, column=2)
# colourLabel.grid(row=5, column=0)
# colourEntry.grid(row=5, column=2)
# vinLabel.grid(row=6, column=0)
# vinEntry.grid(row=6, column=2)
# typeLabel.grid(row=7, column=0)
# typeEntry.grid(row=7, column=2)
# statusLabel.grid(row=8, column=0)
# statusEntry.grid(row=8, column=2)
# siteLabel.grid(row=9, column=0)
# siteEntry.grid(row=9, column=2)
# inspectorLabel.grid(row=10, column=0)
# inspectorEntry.grid(row=10, column=2)
# datetimeLabel.grid(row=11, column=0)
# datetimeEntry.grid(row=11, column=2)
# cancelButton.grid(row=12, column=0)
# acceptButton.grid(row=12, column=2)

# def updateVehiclePane(veh):
#     #   Update Vehicle Details form with loaded record
#     #print("Update vehicle pane: with vehicle "+str(veh.reg)) # output for debugging
#     regEntry.config(text=veh.reg.upper())
#     regEntry.delete(0,"end")
#     makeEntry.delete(0,"end")
#     modelEntry.delete(0,"end")
#     colourEntry.delete(0,"end")
#     vinEntry.delete(0,"end")
#     mileageEntry.delete(0,"end")
#     typeEntry.delete(0,"end")
#     statusEntry.delete(0,"end")
#     siteEntry.delete(0,"end")
#     inspectorEntry.delete(0,"end")
#     datetimeEntry.delete(0,"end")
#     regEntry.insert(0,veh.reg)
#     makeEntry.insert(0,veh.make)
#     modelEntry.insert(0,veh.model)
#     colourEntry.insert(0,veh.colour)
#     vinEntry.insert(0,str(veh.vin))
#     mileageEntry.insert(0,str(veh.mileage))
#     typeEntry.insert(0,veh.type)
#     statusEntry.insert(0,veh.status)
#     siteEntry.insert(0,veh.site)
#     inspectorEntry.insert(0,veh.inspector)
#     datetimeEntry.insert(0,veh.updated)
#     return
  
# def searchvehicle():
#     reg = str(searchEntry.get())
#     print("Searching for "+reg)
#     details.delete("1.0", "end")
#     global foundvan
#     foundvan = vehicle("",reg,"","","","","","","","","","","","")
#     foundvan.read()
#     if foundvan.make !="":
#         databaseFrame.configure( text="Database Results for "+str(foundvan.reg))
#         output = "Comments for "+foundvan.reg
#         details.delete("1.0","end")
#         details.insert("1.0", output+"\n")
#         updateVehiclePane(foundvan)
#         outputcomments = foundvan.getComments()  
#         details.insert("6.0", "\n"+ outputcomments+"\n")
#     else:
#         databaseFrame.configure( text="NO RESULTS for "+str(reg))
#         output="VEHICLE "+reg+" NOT FOUND"
#         details.delete("1.0","end")
#         details.insert("1.0", output)
#     return foundvan

# def updatemile():
#     foundvan.updateMileage(mileageEntry.get()) 

# def addcomment():
#     foundvan.createComment(commentBox.get("1.0","end"))
#     commentBox.delete("1.0","end")
#     pass

# searchButton = tk.Button(searchFrame, padx=5, pady=5, text="SEARCH",command=searchvehicle)
# commentButton =tk.Button(commentFrame, padx=5, pady=5, text="SUBMIT Comment", command=addcomment)
# commentButton.grid(row=1,column=1, columnspan=2)

# details = tk.Text(databaseFrame, height=37, width=60, pady=5,padx=5, bg="light yellow", fg="black")
# details.grid(row=0, column=0)


# # pack form

# searchLabel.grid(row=0, column=0, padx=5, pady=5)
# searchEntry.grid(row=0, column=2, padx=5, pady=5)
# searchButton.grid(row=1,column=2, padx=5, pady=5)
# #
# root.bind('<Return>', (lambda event: searchvehicle()))
# mileageEntry.bind('<Return>',(lambda event: updatemile()))
# commentBox.bind('<Return>',(lambda event:addcomment()))

# root.mainloop()
