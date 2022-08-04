from PIL import Image, ImageOps
import math
import numpy as np

image = Image.open(r"C:\Users\Peanu\OneDrive\Desktop\UncannyEdgeDetection\engine.png")
pixels = image.load()



#Grayscale image
image = ImageOps.grayscale(image)




#Gaussian Filter (Will replace later with an adaptive filter)
k = 2
sigma = 1

kernal = np.array([[math.exp(-(i**2+j**2)/(2*sigma**2))/(2*math.pi*sigma**2) for j in range(-k, k+1)] for i in range(-k, k+1)])
kernal = (kernal*(1/kernal[0][0])).astype(int)


new_image = Image.new('L', image.size, "white")
new_pixels = new_image.load()
for col in range(new_image.size[0]):
    for row in range(new_image.size[1]):
        #Window is pixels that surround the current pixel, 0 if out of bounds
        window = 0
        new_pixels[col, row] = np.sum(np.sum(kernal)*kernal*window)

image = new_image
image.show()




        

