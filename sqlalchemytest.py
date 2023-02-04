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
        print("UPD MILEAGE   : on "+self.reg+" from "+str(self.mileage)+" to "+str(newmileage))
        oldmileage = self.mileage
        self.mileage = newmileage
        self.addComment("Mileage Updated from "+str(oldmileage)+" to "+str(self.mileage),"Mileage Update")
        self.updatedby = "+Mileage Update"
        self.updatedon = str(timenow)
        session.commit()
    def addComment(self, commenttoadd, commentuser):
        timenow = str(datetime.now())
        print("ADD COMMENT   : on "+self.reg+" at "+str(self.mileage)+" MILES "+commenttoadd)
        newcomment = Comment(random.randint(0,999999), commenttoadd,commentuser,timenow,self.reg)
        session.add(newcomment)
        self.updatedby = "+Comment #"+str(newcomment.commentid)
        self.updatedon = timenow
        session.commit()
    def addInspection(self, inspector, location, mileage, bodywork, lights, osf, osr, nsr, nsf, doors, windwipers, extmirrors, extnotes,oil, coolant, screenwash, engnotes, adblue, horn, steering, brakes, handbrake, seatbelts, controls, firstaid, intnotes, insnotes):
        timenow = str(datetime.now())
        newinspection = Inspection(random.randint(0,999999),self.reg,timenow, inspector, location, mileage, bodywork, lights, osf, osr, nsr, nsf, doors, windwipers, extmirrors, extnotes,oil, coolant, screenwash, engnotes, adblue, horn, steering, brakes, handbrake, seatbelts, controls, firstaid, intnotes, insnotes)
        self.updatedby = "+Inspection #"+str(newinspection.inspectionid)
        self.updatedon = timenow
        self.mileage = newinspection.mileage
        print("ADD INSPECT   :"+self.reg+" at "+str(self.mileage)+" by "+newinspection.inspector+" at "+newinspection.insdatetime)
        self.addComment("Inspection #"+str(newinspection.inspectionid)+" added to vehicle","Inspection")
        session.add(newinspection)
        session.commit()
class Comment(Base):
    __tablename__ = "comments"

    commentid = Column("commentid", Integer, Identity(start=1000,cycle=True),primary_key=True)
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
class Inspection(Base):
    __tablename__ = "inspections"

    # General Inspection Information Portion

    inspectionid = Column("inspectionid", Integer, Identity(start=10000, cycle=True),primary_key=True)
    reg = Column(String(7),ForeignKey(Vehicle.reg))
    insdatetime = Column("insdatetime",String(26))
    inspector = Column("inspector",String(20))
    location = Column("location",String(10))
    mileage = Column("mileage",Integer)
    
    # Exterior Checks Portion

    bodywork = Column("bodywork",CHAR)
    lights = Column("lights",CHAR)
    osf = Column("osf",String(3))
    osr = Column("osr",String(3))
    nsr = Column("nsr",String(3))
    nsf = Column("nsf",String(3))
    doors = Column("doors",CHAR)
    windwipers = Column("windwipers",CHAR)
    extmirrors = Column("extmirrors",CHAR)
    extnotes = Column("extnotes", String(30))
    
    # Engine Bay Portion

    oil = Column("oil",CHAR)
    coolant = Column("coolant",CHAR)
    screenwash = Column("screenwash",CHAR)
    engnotes = Column("engnotes",String(30))

    # Interior Checks Portion

    adblue = Column("adblue",CHAR)
    horn = Column("horn",CHAR)
    steering = Column("steering",CHAR)
    brakes = Column("brakes",CHAR)
    handbrake = Column("handbrake",CHAR)
    seatbelts = Column("seatbelts",CHAR)
    controls = Column("controls",CHAR)
    firstaid = Column("firstaid",CHAR)
    intnotes = Column("intnotes",String(30))
        
    insnotes = Column("insnotes", String(30))

    def __init__(self, inspectionid, reg, insdatetime, inspector, location, mileage, bodywork, lights, osf, osr, nsr, nsf, doors, windwipers, extmirrors, extnotes,
        oil, coolant, screenwash, engnotes,
        adblue, horn, steering, brakes, handbrake, seatbelts, controls, firstaid, intnotes, insnotes):
        
        self.inspectionid = inspectionid
        self.reg = reg
        self.insdatetime = insdatetime
        self.inspector = inspector
        self.location = location
        self.mileage = mileage
        self.bodywork = bodywork
        self.lights = lights
        self.osf = osf
        self.osr =osr
        self.nsr =nsr
        self.nsf = nsf
        self.doors = doors
        self.windwipers = windwipers
        self.extmirrors = extmirrors
        self.extnotes = extnotes
        self.oil = oil
        self.coolant = coolant
        self.screenwash = screenwash
        self.engnotes = engnotes
        self.adblue = adblue
        self.horn = horn
        self.steering = steering
        self.brakes = brakes
        self.handbrake = handbrake
        self.seatbelts = seatbelts
        self.controls = controls
        self.firstaid = firstaid
        self.intnotes = intnotes
        self.insnotes = insnotes

def makeconnection(): # Make connection to DB and RETURN the session
    print("DB            :CONNECTING...")
    engine= create_engine(str(connectionstring))
    print("DB            :CONECTED - Binding to engine")
    Base.metadata.create_all(bind=engine)
    print("SESSION       :CREATING SESSION")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
def loadvehicle(reg): # takes GLOBAL session from makeconnection() and loads vehicle from DB into a Vehicle object
    vehicle = session.query(Vehicle).filter(Vehicle.reg == reg).first()
    if not vehicle:
        print("QUERY         :NO RESULTS FOUND")
    else:
        print("LD REC        :Found van "+vehicle.reg+" with mileage : "+str(vehicle.mileage))
    return vehicle

# MAIN PROGRAM LOOP STARTS HERE


updatingreg = "XX11XXX"

timenow = str(datetime.now())

session = makeconnection()
#van = Vehicle(updatingreg,"TechnoShed","EV-01","Grey",4,2023,"TEST","Grimsby","DEV TEAM",timenow)
#session.add(van)
#savechanges()

foundvan = loadvehicle(updatingreg) # load a van into class


print("              :Trying new functions")

# foundvan.addComment("This is another comment","gaylord bummer")

foundvan.updateMileage(foundvan.mileage+666)

# firstinspection = Inspection(random.randint(0,999999),foundvan.reg,timenow,"Karl Winstanley","Meridian",16000,"X","O","OK","OK","OK","WRN","O","O","X","NS Mirror smashed","O","O","T","","O","O","O","O","O","O","O","M","Dirty Interior","First Insepction on this bus")

inspect1= foundvan.addInspection("Karl Winstanley","Meridian",foundvan.mileage,"X","O","WRN","OK","OK","WRN","O","O","X","NS Mirror smashed","O","O","T","","O","O","O","O","O","O","O","M","Dirty Interior","Test Inspection via method")
