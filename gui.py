import tkinter as tk

# TKinter portion GUI

# DEFINE root window

root=tk.Tk()
root.title("TechnoShed Studios - Fleet Vehicle Database")
#root.geometry('1010x620')
root.resizable(width=0,height=0)
    
# DEFINE Main Frames

vehicledetailsFrame = tk.LabelFrame(root ,text="Vehicle Details",width=120, borderwidth=5, relief="ridge")
commentsFrame = tk.LabelFrame(root, text="Vehicle Log",borderwidth=5, relief="ridge")
inspectionsFrame = tk.LabelFrame(root, text="Vehicle Inspections",borderwidth=5, relief="ridge")

inspectionslistFrame = tk.Frame(inspectionsFrame)
inspectionsdetailFrame = tk.LabelFrame(inspectionsFrame, text="Inspection Detail", relief="ridge")

# GRID place frames in root window

vehicledetailsFrame.grid(row=0, column=0, columnspan=3,padx=5,pady=5, sticky="NESW")
inspectionsFrame.grid(row=1, column=0, columnspan=3,padx=5,pady=5, sticky="NESW")
commentsFrame.grid(row=2, column=0, columnspan=3,padx=5,pady=5, sticky="NESW")
inspectionslistFrame.grid(row=0, column=0)
inspectionsdetailFrame.grid(row=0,column=1, columnspan=2,padx=5,pady=5, sticky="NWES")


# DEFINE vehicledetailsFrame

regLabel = tk.Label(vehicledetailsFrame, width=20, text="Registration")
regEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
mileageLabel = tk.Label(vehicledetailsFrame, width=20, text="Mileage")
mileageEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
makeLabel = tk.Label(vehicledetailsFrame, width=20, text="Make")
makeEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
modelLabel = tk.Label(vehicledetailsFrame, width=20, text="Model")
modelEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
colourLabel = tk.Label(vehicledetailsFrame, width=20, text="Colour")
colourEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
vinLabel = tk.Label(vehicledetailsFrame, width=20, text="VIN")
vinEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
typeLabel = tk.Label(vehicledetailsFrame, width=20, text="Type")
typeEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
statusLabel = tk.Label(vehicledetailsFrame, width=20, text="Status")
statusEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
siteLabel = tk.Label(vehicledetailsFrame, width=20, text="Site")
siteEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
inspectorLabel = tk.Label(vehicledetailsFrame, width=20, text="Updated by")
inspectorEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")
datetimeLabel = tk.Label(vehicledetailsFrame, width=20, text="Updated at")
datetimeEntry = tk.Entry(vehicledetailsFrame, width=25, bg="light yellow", fg="black")

# GRID place widgets in vehciledetailsFrame

regLabel.grid(row=0, column=0,padx=5,pady=5)
regEntry.grid(row=0, column=1,padx=5,pady=5)
mileageLabel.grid(row=0, column=2,padx=2,pady=2)
mileageEntry.grid(row=0, column=3,padx=2,pady=2)
makeLabel.grid(row=1, column=0)
makeEntry.grid(row=1, column=1)
modelLabel.grid(row=2, column=0)
modelEntry.grid(row=2, column=1)
colourLabel.grid(row=3, column=0)
colourEntry.grid(row=3, column=1)
vinLabel.grid(row=2, column=2)
vinEntry.grid(row=2, column=3)
typeLabel.grid(row=3, column=2)
typeEntry.grid(row=3, column=3)
statusLabel.grid(row=4, column=0)
statusEntry.grid(row=4, column=1)
siteLabel.grid(row=4, column=2)
siteEntry.grid(row=4, column=3)
inspectorLabel.grid(row=5, column=0)
inspectorEntry.grid(row=5, column=1)
datetimeLabel.grid(row=5, column=2)
datetimeEntry.grid(row=5, column=3)


# POPULATE inspectionslistFrame

inspectionslist = tk.Text(inspectionslistFrame, height=15, width=40, bg="light yellow", fg="black")
inspectionslist.grid(row=0, column=0,padx=5,pady=5)

# DEFINE inspectionsdetailsFrame widgets

insmileageLabel = tk.Label(inspectionsdetailFrame, width=10, text="Mileage")
inspectorLabel = tk.Label(inspectionsdetailFrame, width=10, text="Inspector")
insdatetimeLabel = tk.Label(inspectionsdetailFrame, width=10, text="Date Time")
inslocationLabel = tk.Label(inspectionsdetailFrame, width=10, text="Location")
bodyworkLabel = tk.Label(inspectionsdetailFrame, width=10, text="Bodywork")
bodyworkEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
lightsLabel = tk.Label(inspectionsdetailFrame, width=10, text="Lights")
lightsEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")

osfLabel = tk.Label(inspectionsdetailFrame, width=8, text="OSF Tyre")
osrLabel = tk.Label(inspectionsdetailFrame, width=8, text="OSR Tyre")
nsrLabel = tk.Label(inspectionsdetailFrame, width=8, text="NSR Tyre")
nsfLabel = tk.Label(inspectionsdetailFrame, width=8, text="NSF Tyre")
tyresLabel = tk.Label(inspectionsdetailFrame, text="Tyres")

doorsLabel = tk.Label(inspectionsdetailFrame, width=10, text="Doors")
doorsEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
windLabel = tk.Label(inspectionsdetailFrame, width=10, text="Windows")
windEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
extmirrorLabel = tk.Label(inspectionsdetailFrame, width=10, text="Mirrors")
extmirrorEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
extnotesLabel = tk.Label(inspectionsdetailFrame, width=10, text="EXT notes")
extnotesEntry = tk.Entry(inspectionsdetailFrame, width=25, bg="light yellow", fg="black")

oilLabel = tk.Label(inspectionsdetailFrame, width=10, text="Oil Level")
oilEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
coolantLabel = tk.Label(inspectionsdetailFrame, width=10, text="Coolant")
coolantEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
screenwashLabel = tk.Label(inspectionsdetailFrame, width=10, text="Screenwash")
screenwashEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
engnoteLabel = tk.Label(inspectionsdetailFrame, width=10, text="Engine Bay Comments")
engnotesEntry = tk.Entry(inspectionsdetailFrame, width=25, bg="light yellow", fg="black")

adblueLabel = tk.Label(inspectionsdetailFrame, width=20, text="Adblue")
adblueEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
hornLabel = tk.Label(inspectionsdetailFrame, width=20, text="Horn")
hornEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
steeringLabel = tk.Label(inspectionsdetailFrame, width=20, text="Steering")
steeringEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
brakesLabel = tk.Label(inspectionsdetailFrame, width=20, text="Brakes")
brakesEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
handbrakeLabel = tk.Label(inspectionsdetailFrame, width=20, text="Hand Brake")
handbrakeEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
seatbeltsLabel = tk.Label(inspectionsdetailFrame, width=20, text="Seat belts")
seatbeltsEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
controlssLabel = tk.Label(inspectionsdetailFrame, width=20, text="Controls")
controlsEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
firstaidLabel = tk.Label(inspectionsdetailFrame, width=20, text="First Aid Kit")
firstaidEntry = tk.Entry(inspectionsdetailFrame, width=6, bg="light yellow", fg="black")
intnotesLabel = tk.Label(inspectionsdetailFrame, width=20, text="Interior Notes")
intnotesEntry = tk.Entry(inspectionsdetailFrame, width=25, bg="light yellow", fg="black")

insnotesLabel = tk.Label(inspectionsdetailFrame, width=20, text="Inspection Comments")
insnotesEntry = tk.Entry(inspectionsdetailFrame, width=25, bg="light yellow", fg="black")

# GRID place inspectiondetailsFrame widgets

inspectorLabel.grid(row=0, column=0, sticky="NW")
insdatetimeLabel.grid(row=0,column=2)
inslocationLabel.grid(row=0, column=4)
insmileageLabel.grid(row=0, column=6)
bodyworkLabel.grid(row=1,column=0)
bodyworkEntry.grid(row=1,column=1)
lightsLabel.grid(row=1,column=2)
lightsEntry.grid(row=1,column=3)
doorsLabel.grid(row=1, column=4)
doorsEntry.grid(row=1, column=5)
extmirrorLabel.grid(row=1, column=6)
extmirrorEntry.grid(row=1, column=7)
windLabel.grid(row=2,column=0)
windEntry.grid(row=2,column=1)
extnotesLabel.grid(row=2,column=2, sticky="W")
engnoteLabel.grid(row=7, column=0)
extnotesEntry.grid(row=2, column=3, columnspan=5, sticky="NESW")



# TYRES gui block

tyresLabel.grid(row=13,column=6, columnspan=2)
nsfLabel.grid(row=14,column=6)
osfLabel.grid(row=14,column=7)
nsrLabel.grid(row=15,column=6)
osrLabel.grid(row=15,column=7)

# ENGINE bay block

oilLabel.grid(row=6, column=0)
oilEntry.grid(row=6,column=1)
coolantLabel.grid(row=6,column=2)
coolantEntry.grid(row=6, column=3)
adblueLabel.grid(row=6,column=4)
adblueEntry.grid(row=6,column=5)
screenwashLabel.grid(row=6,column=6)
screenwashEntry.grid(row=6,column=7)


# POPULATE commentsFrame

commentBox= tk.Text(commentsFrame,  height=5, width=121, bg="light yellow", fg="black")
commentBox.grid(row=0, column=0, columnspan=3,padx=5,pady=5)



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

root.mainloop()
