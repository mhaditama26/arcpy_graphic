#this tools made by didit_indonesia
#vizualizing graphic bar data on arcgis layout
#GeoCircle_Indonesia

import arcpy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#definition parameter
mxd = arcpy.mapping.MapDocument(r"go to your project arcGIS file (.mxd)")
a = arcpy.mapping.ListLayoutElements(mxd,"PICTURE_ELEMENT")
shp =  arcpy.MakeFeatureLayer_management(r"go to your shapefile file (.shp)")

#before you run this script , create the project arcgis with layout and insert some picture and named it on properties as "test"
#process
#looping on data driven pages
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    pageName = mxd.dataDrivenPages.pageRow.getValue("FID")
    print (pageName)
    #select row data to vizualize
    arcpy.SelectLayerByAttribute_management(shp  ,"NEW_SELECTION",'
"FID" = '+ repr(pageName))
    #create array class
    #choose field that you want to build graphic                                     
    arr = arcpy.da.FeatureClassToNumPyArray(shp, ['field1','field2'])
    #create data frame
    df = pd.DataFrame(arr)
    df.columns.names=['field2']
    #create plot
    df.plot(x='field1',kind='bar')
    plt.savefig(r"your direction folder"+str(pageNum)+".png")
    #change graphic for each page
    for elm in a:
        if elm.name == "test":
            elm.sourceImage =
r"your direction folder/"+str(pageNum)+".png"
            arcpy.mapping.ExportToPNG(mxd,
r"your direction folder/"+str(pageNum)+".png")
