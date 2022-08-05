from PIL import Image, ImageOps
import math
import numpy as np

x = -22.4
    
print((x+22.5)//45*45)
quit()



image = Image.open(r"C:\Users\Peanu\OneDrive\Desktop\UncannyEdgeDetection\engine.png")




#Grayscale image------------------------------------------------------------------------------------------
image = ImageOps.grayscale(image)
pixels = image.load()



#Gaussian Filter (Will replace later with an adaptive filter)---------------------------------------------
k = 2
sigma = 1

kernal = np.array([[math.exp(-(i**2+j**2)/(2*sigma**2))/(2*math.pi*sigma**2) for j in range(-k, k+1)] for i in range(-k, k+1)])
kernal = (kernal*(1/kernal[0][0])).astype(int)
new_image = Image.new('L', image.size, "white")
new_pixels = new_image.load()

for col in range(new_image.size[0]):
    for row in range(new_image.size[1]):
        #Pixels from original image being averaged, -1 if out of bounds
        window = np.array([[pixels[col+c,row+r] if (0 <= col+c < new_image.size[0] and 0 <= row+r < new_image.size[1]) else -1 for c in range(-k, k+1)] for r in range(-k, k+1)])

        #Total of all weights being used, does't contain weights of positions out of bounds (-1 in window)
        total = sum([sum([kernal[r][c] if window[r][c] != -1 else 0 for c in range(2*k+1)]) for r in range(2*k+1)])

        new_pixels[col,row] = int(np.sum(kernal*window.clip(min=0))/total)
                
image = new_image
image.show()


#Intensity Gradient using Sobel Filter--------------------------------------------------------------------
new_image = Image.new('L', image.size, "white")
new_pixels = new_image.load()

xkernal = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
ykernal = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])

gradients = np.empty((image.size[1], image.size[0]))
angles = np.empty((image.size[1], image.size[0]))

for col in range(new_image.size[0]):
    for row in range(new_image.size[1]):
        window = np.array([[pixels[col+c,row+r] if (0 <= col+c < new_image.size[0] and 0 <= row+r < new_image.size[1]) else -1 for c in range(-1, 2)] for r in range(-1, 2)])
        gx = np.sum(window*xkernal)
        gy = np.sum(window*ykernal)
        
        G = math.sqrt(gx**2 + gy**2)
        theta = math.atan2(gy, gx)

        new_pixels[col,row] = int(G)
        gradients[row][col] = G
        angles[row][col] = theta

image = new_image
image.show()
        

#Non-maximum Suppression-----------------------------------------------------------------------------------
new_image = Image.new('L', image.size, "white")
new_pixels = new_image.load()

for col in range(new_image.size[0]):
    for row in range(new_image.size[1]):
        pass
        
        


image = new_image
image.show()





























        

