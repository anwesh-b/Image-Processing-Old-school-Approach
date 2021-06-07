#Base code for how to import and manipulate the image

from PIL import Image as im
import numpy as np

colors = ['Red','Green','Blue']
colorImage = '../input.jpg'
bwImage = './bwInput.jpg'

def getNpArrayFromImage(imageSource):
    img = im.open(imageSource)
    return np.asarray(img)

def extractNegativeImage(image, typeOfNegative):
    print("Extracting for " + typeOfNegative + " negative")
    newImagearray = []

    for i in range(0,len(image)):
        row = []  
        for j in range(0,len(image[i])):
            pixel = []
            pixel.append(np.uint8(255-image[i][j][0]))
            pixel.append(np.uint8(255-image[i][j][1]))
            pixel.append(np.uint8(255-image[i][j][2])) 
            row.append(pixel)
            #Do not forget to use np.uint8() to convert int to uint8 data type
        print("Working on row: "+str(i))
        newImagearray.append(np.asarray(row))

    return np.asarray(newImagearray)  

def extractNegativeBWImage(image, typeOfNegative):
    print("Extracting for " + typeOfNegative + " negative")
    newImagearray = []

    for i in range(0,len(image)):
        row = []  
        for j in range(0,len(image[i])):
            row.append(np.uint8(255-image[i][j]))
            #Do not forget to use np.uint8() to convert int to uint8 data type
        print("Working on row: "+str(i))
        newImagearray.append(np.asarray(row))

    return np.asarray(newImagearray) 

def saveImage( npArrayImage, typeOfNegative):
    image = im.fromarray(npArrayImage)
    print("Saving for " + typeOfNegative + " negative")
    image.save(typeOfNegative+'Negative.jpg')
    return

def main():
    image = getNpArrayFromImage(colorImage)
    extractedImage = extractNegativeImage(image, 'color')
    saveImage( extractedImage, 'color')
    image = getNpArrayFromImage(bwImage)
    extractedImage = extractNegativeBWImage(image, 'black and white')
    saveImage( extractedImage, 'black and white')
    print("THANK YOU!!!!!")


if __name__ == "__main__":
    main() 
