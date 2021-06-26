#Base code for how to import and manipulate the image

from PIL import Image as im
import numpy as np
import matplotlib.pyplot as plt

bwImage = '../bwInput.jpg'

def getNpArrayFromImage(imageSource):
    img = im.open(imageSource)
    return np.asarray(img)

def histogram(image):
    histogramArray = [0]*256

    for i in range(0,len(image)):
        for j in range(0,len(image[i])):
            histogramArray[np.uint8(image[i][j])] = histogramArray[np.uint8(image[i][j])] + 1
            #Do not forget to use np.uint8() to convert int to uint8 data type
        if i%10==0:
            print("Completed row: "+str(i))

    return histogramArray 

def histogramEqualization(originalImage, histogramArray):
    totalPixel = sum(histogramArray)
    print("totalPixel")
    print(totalPixel)

    for i in range(0,len(histogramArray)):
        histogramArray[i] = (histogramArray[i] /totalPixel )
    
    for i in range(1,len(histogramArray)):
        histogramArray[i] = histogramArray[i] + histogramArray[i-1] 

    for i in range(0,len(histogramArray)):
        histogramArray[i] = round(histogramArray[i] *255 ) 
        print(histogramArray[i])
    
    equalizedHisto = [0]*256

    newImage = []
    for i in range(0,len(originalImage)):
        row = []
        for j in range(0,len(originalImage[i])):
            row.append(np.uint(histogramArray[originalImage[i][j]]))
            equalizedHisto[row[j]] = equalizedHisto[row[j]] + 1
        newImage.append(np.asarray(row))

    plt.plot(equalizedHisto)
    plt.xlabel('Intensity')
    plt.ylabel('No of pixel')
    plt.savefig('EqualizedHistogramGraph.jpg')
    plt.show()

    return np.asarray(newImage)
    


def saveImage( npArrayImage):
    image = im.fromarray(npArrayImage.astype(np.uint8))
    print("Saving Histogram Equalized image")
    image.save('HistogramEqualized.jpg')
    return

def main():
    image = getNpArrayFromImage(bwImage)
    histogramArray = histogram(image)
    equalizedImage = histogramEqualization(image, histogramArray)
    # equalizedImage = histogramEqualization(histogramArray)
    saveImage(equalizedImage)
    print("THANK YOU!!!!!")


if __name__ == "__main__":
    main() 
