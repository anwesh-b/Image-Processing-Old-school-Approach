#Base code for how to import and manipulate the image

from PIL import Image as im
import numpy as np

img = im.open('download.jpg')
numpydata = np.asarray(img)
  
newImagearray = []
for i in range(0,1024):
    row = []  
    for j in range(0,1024):
        pixel = []
        pixel.append(numpydata[i][j][0])
        pixel.append(numpydata[i][j][1])
        pixel.append(numpydata[i][j][2]) 
        #Do not forget to use np.uint8() to convert int to unit8 data type
        row.append(pixel)
    print("Working on row: "+str(i))
    newImagearray.append(np.asarray(row))

img = np.asarray(newImagearray)

image = im.fromarray(img)

image.save('output.jpg')
