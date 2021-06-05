#Base code for how to import and manipulate the image

from PIL import Image as im
import numpy as np

originalImage = '../input.jpg'

def avg(arraysss):
    return sum(arraysss)/len(arraysss)

bwAlgos = [min,max,avg]


def getNpArrayFromImage(imageSource):
    img = im.open(imageSource)
    return np.asarray(img)

def extractColor(image, algo):
    print("Extracting using : " + algo.__name__)
    newImagearray = []

    for i in range(0,len(image)):
        row = []  
        for j in range(0,len(image[i])):
            row.append(np.uint8(algo(image[i][j])))
        print("Working on row: "+str(i))
        newImagearray.append(np.asarray(row))

    return np.asarray(newImagearray)  

def saveImage(npArrayImage, algo):
    image = im.fromarray(npArrayImage)
    print("Saving using algo : " + algo.__name__)
    image.save(algo.__name__ + '-output.jpg')
    return

def main():
    image = getNpArrayFromImage(originalImage)
    for algo in bwAlgos:
        extractedImage = extractColor(image, algo)
        saveImage(extractedImage, algo)
    print("THANK YOU!!!!!")


if __name__ == "__main__":
    main() 
