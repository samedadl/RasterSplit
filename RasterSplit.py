# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:20:03 2021

@author: Samed
"""

from osgeo import gdal

img = gdal.Open("Renkli_MS.tif")
gt = img.GetGeoTransform()

# get coordinates of upper left corner
xmin = gt[0]
ymax = gt[3]
res = gt[1]

# determine total length of raster
xlen = res * img.RasterXSize
ylen = res * img.RasterYSize

# number of tiles in x and y direction
xdiv = 2
ydiv = 2

# size of a single tile
xsize = xlen/xdiv
ysize = ylen/ydiv

# create lists of x and y coordinates
xsteps = [xmin + xsize * i for i in range(xdiv+1)]
ysteps = [ymax - ysize * i for i in range(ydiv+1)]

# loop over min and max x and y coordinates
for i in range(xdiv):
    for j in range(ydiv):
        xmin = xsteps[i]
        xmax = xsteps[i+1]
        ymax = ysteps[j]
        ymin = ysteps[j+1]
        
        # print("xmin: "+str(xmin))
        # print("xmax: "+str(xmax))
        # print("ymin: "+str(ymin))
        # print("ymax: "+str(ymax))
        # print("\n")
        
        # use gdal warp
        # gdal.Warp("MSsa"+str(i)+str(j)+".tif", img, xRes = res, yRes = -res,
        #           outputBounds = (xmin, ymin, xmax, ymax), dstNodata = -9999)
        # or gdal translate to subset the input raster
        gdal.Translate("MSimg_translate"+str(i)+str(j)+".tif", img, projWin = (xmin, ymax, xmax, ymin), 
                       xRes = res, yRes = -res)
 
# close the open dataset!!!
img = None