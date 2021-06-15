#Base code for how to import and manipulate the image

from PIL import Image as im
import numpy as np

colorImage = '../input.jpg'
bwImage = '../bwInput.jpg'
gamma = 2
maxGamma = pow(255, gamma)

def getNpArrayFromImage(imageSource):
    img = im.open(imageSource)
    return np.asarray(img)

def transformPixel(pixelll):
    x = round(pow(pixelll, gamma)*255 /maxGamma)
    return x 

def powerTransformation(image, typeOfImage):
    print("Transforming for " + typeOfImage + " using power law")
    newImageArray = []

    for i in range(0,len(image)):
        row = []  
        for j in range(0,len(image[i])):
            if typeOfImage == 'color':
                pixel = []
                pixel.append(np.uint8(transformPixel(image[i][j][0])))
                pixel.append(np.uint8(transformPixel(image[i][j][1])))
                pixel.append(np.uint8(transformPixel(image[i][j][2])))  
                row.append(pixel)
            else:
                row.append(np.uint8(transformPixel(image[i][j]))) 
            #Do not forget to use np.uint8() to convert int to uint8 data type
        if i%10==0:
            print("Completed row: "+str(i))
        newImageArray.append(np.asarray(row))

    return np.asarray(newImageArray)  


def saveImage( npArrayImage, typeOfImage):
    image = im.fromarray(npArrayImage.astype(np.uint8))
    print("Saving for " + typeOfImage)
    image.save(typeOfImage+'.jpg')
    return

def main():
    image = getNpArrayFromImage(colorImage)
    extractedImage = powerTransformation(image, 'color')
    saveImage( extractedImage, 'color power law')
    image = getNpArrayFromImage(bwImage)
    extractedImage = powerTransformation(image, 'black and white')
    saveImage( extractedImage, 'black and white power law')
    print("THANK YOU!!!!!")


if __name__ == "__main__":
    main() 
