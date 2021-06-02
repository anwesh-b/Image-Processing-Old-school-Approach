#Base code for how to import and manipulate the image

from PIL import Image as im
import numpy as np

colors = ['Red','Green','Blue']
originalImage = '../input.jpg'

def getNpArrayFromImage(imageSource):
    img = im.open(imageSource)
    return np.asarray(img)

def extractColor(color,image):
    print("Extracting for color: "+color)
    newImagearray = []
    pos = colors.index(color)

    for i in range(0,len(image)):
        row = []  
        for j in range(0,len(image[i])):
            pixel = []
            pixel.append(np.uint8(0))
            pixel.append(np.uint8(0))
            pixel.append(np.uint8(0)) 
            pixel[pos] = image[i][j][pos]
            row.append(pixel)
            #Do not forget to use np.uint8() to convert int to uint8 data type
        print("Working on row: "+str(i))
        newImagearray.append(np.asarray(row))

    return np.asarray(newImagearray)  

def saveImage(color, npArrayImage):
    image = im.fromarray(npArrayImage)
    print("Saving for color: "+color)
    image.save(color+'Output.jpg')
    return

def main():
    image = getNpArrayFromImage(originalImage)
    for color in colors:
        extractedImage = extractColor(color, image)
        saveImage(color, extractedImage)
    print("THANK YOU!!!!!")


if __name__ == "__main__":
    main() 
