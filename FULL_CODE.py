# Import Modules and set current workspace
import arcpy
from arcpy import env
import os

arcpy.env.overwriteOutput = True

env.workspace = "G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb"

# Define Variables and List of Tables in our Geodatabase
inFeatures = "G:\\Share\\GEOG6293\ross\\ADD_LYR\Python_Project.gdb\\Lower_48_Blank"
i = 0
layerName = "Lower_48"
names = ["Y07_08","Y08_09","Y09_10","Y10_11","Y11_12","Y12_13","Y13_14"]
field_list = arcpy.ListTables()
print names
print field_list


# For loop iterating through our tables and adding them to the shapefile "Lower_48"
for Layer_Name in field_list:
    arcpy.MakeFeatureLayer_management (inFeatures, names[i]) #Temp
    arcpy.AddJoin_management(names[i], "STATE_FIPS", field_list[i], "STATE_FIPS", "KEEP_ALL")
    arcpy.SelectLayerByAttribute_management(names[i], "NEW_SELECTION")
    arcpy.CopyFeatures_management(inFeatures, names[i])
    i = i+ 1

print "This is the list of newly joined tables."
LF = arcpy.ListFeatureClasses()
print LF

print "Complete"

# Add the layer we just created to the premade maps

AddLayer = []
writeLog=open("G:\Share\GEOG6293\ross\ADD_LYR"+"\FileListLog.txt","w")
for fileName in os.listdir("G:\Share\GEOG6293\ross\ADD_LYR"):
    fullPath = os.path.join("G:\Share\GEOG6293\ross\ADD_LYR", fileName)
    if os.path.isfile(fullPath):
        basename, extension = os.path.splitext(fullPath)
        if extension == ".mxd":
            writeLog.write("G:\Share\GEOG6293\ross\ADD_LYR"+"\n")
            mxd = arcpy.mapping.MapDocument(fullPath)
            AddLayer +=[fileName]
print AddLayer

i = 0
Joined_Table = ["G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb/Y07_08"
,"G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb/Y08_09",
"G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb/Y09_10",
"G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb/Y10_11",
"G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb/Y11_12",
"G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb/Y12_13",
"G:\Share\GEOG6293\ross\ADD_LYR\Python_Project.gdb/Y13_14"]

for stuff in AddLayer[0:7]:
        path = "G:\\Share\\GEOG6293\\ross\\ADD_LYR\\" + stuff
        mxd = arcpy.mapping.MapDocument(path)
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        addLayer = arcpy.mapping.Layer(Joined_Table[i])
        arcpy.mapping.AddLayer(df, addLayer, "TOP")
        mxd.save()
        i = i+ 1

for stuffs in AddLayer[8:14]:
        path = "G:\\Share\\GEOG6293\\ross\\ADD_LYR\\" + stuffs
        mxd = arcpy.mapping.MapDocument(path)
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        addLayer = arcpy.mapping.Layer(Joined_Table[i])
        arcpy.mapping.AddLayer(df, addLayer, "TOP")
        mxd.save()
        i = i+ 1

#Write MXD names in folder to txt log file again.
#Export maps to pdf


Maps = []
writeLog=open("G:\Share\GEOG6293\ross\ADD_LYR"+"\FileListLog.txt","w")
for fileName in os.listdir("G:\Share\GEOG6293\ross\ADD_LYR"):
    fullPath = os.path.join("G:\Share\GEOG6293\ross\ADD_LYR", fileName)
    if os.path.isfile(fullPath):
        basename, extension = os.path.splitext(fullPath)
        if extension == ".mxd":
            writeLog.write("G:\Share\GEOG6293\ross\ADD_LYR"+"\n")
            mxd = arcpy.mapping.MapDocument(fullPath)
            Maps +=[fileName]
print Maps

i = 0
names = ["B_07.pdf","B_08.pdf","B_09.pdf","B_10.pdf","B_11.pdf",
"B_12.pdf","B_13.pdf","G_07.pdf","G_08.pdf","G_09.pdf","G_10.pdf"
,"G_11.pdf","G_12.pdf","G_13.pdf"]

for mxd_name in Maps:
     path = "G:\\Share\\GEOG6293\\ross\\ADD_LYR\\" + mxd_name
     outpath ="G:\Share\GEOG6293\ross\ADD_LYR\Outputs\\" + names[i]
     mxd = arcpy.mapping.MapDocument(path)
     arcpy.mapping.ExportToPDF(mxd, names[i])
     i = i+ 1
