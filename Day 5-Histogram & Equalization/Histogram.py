#Base code for how to import and manipulate the image

from PIL import Image as im
import numpy as np
import matplotlib.pyplot as plt

bwImage = '../bwInput.jpg'

def getNpArrayFromImage(imageSource):
    img = im.open(imageSource)
    return np.asarray(img)

def histogram(image):
    print("Using Histogram algorithm ")
    histogramArray = [0]*256

    for i in range(0,len(image)):
        for j in range(0,len(image[i])):
            histogramArray[np.uint8(image[i][j])] = histogramArray[np.uint8(image[i][j])]+1
        if i%10==0:
            print("Completed row: "+str(i))

    # TODO print the histogram 
    # for i in range(0,255):
    #     print("With intensity {intensity}, no of pixels = {intensityPixels}".format(intensity=i, intensityPixels=histogramArray[i] ))
    plt.plot(histogramArray)
    plt.xlabel('Intensity')
    plt.ylabel('No of pixel')
    plt.show()
    plt.savefig('OriginalHistogram.jpg')
    return

def main():
    image = getNpArrayFromImage(bwImage)
    histogram(image)
    print("THANK YOU!!!!!")


if __name__ == "__main__":
    main() 
