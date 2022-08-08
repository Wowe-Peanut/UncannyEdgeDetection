from PIL import Image, ImageOps
import math
import numpy as np
import imageio
import random











def trace_image(image):
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

    

    #Intensity Gradient using Sobel Filter--------------------------------------------------------------------
    new_image = Image.new('L', image.size, "white")
    new_pixels = new_image.load()

    xkernal = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
    ykernal = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])

    gradients = np.empty((image.size[1], image.size[0]))
    angles = np.empty((image.size[1], image.size[0]))

    for col in range(new_image.size[0]):
        for row in range(new_image.size[1]):
            window = np.array([[pixels[col+c,row+r] if (0 <= col+c < new_image.size[0] and 0 <= row+r < new_image.size[1]) else 0 for c in range(-1, 2)] for r in range(-1, 2)])
            gx = np.sum(window*xkernal)
            gy = np.sum(window*ykernal)
            
            G = math.sqrt(gx**2 + gy**2)

            #Round to nearest axis (vertical, horizontal, either diagonals)
            theta = math.atan2(gy, gx)*180/math.pi
            if theta < 0:
                theta += 180
            theta = (theta+22.5)//45*45
            if theta == 180:
                theta = 0
            
            
            new_pixels[col,row] = int(G)
            gradients[row][col] = G
            angles[row][col] = theta

    image = new_image
    pixels = image.load()

    

    #Non-maximum Suppression-----------------------------------------------------------------------------------
    #At every pixel, it suppresses the edge strength of the center pixel
    #(by setting its value to 0) if its magnitude is not greater than the magnitude of the two neighbors in the gradient direction
    new_image = Image.new('L', image.size, "white")
    new_pixels = new_image.load()
                          
    for col in range(new_image.size[0]):
        for row in range(new_image.size[1]):
            angle = angles[row][col]*math.pi/180
            
            #Neighbors in gradient direction
            ndx = round(math.cos(angle))
            ndy = round(math.sin(angle))
            n1 = gradients[row+ndy][col+ndx] if 0 <= row+ndy < image.size[1] and 0 <= col+ndx < image.size[0] else 0
            n2 = gradients[row-ndy][col-ndx] if 0 <= row-ndy < image.size[1] and 0 <= col-ndx < image.size[0] else 0
            if gradients[row][col] < n1 or gradients[row][col] < n2:
                new_pixels[col,row] = 0
                gradients[row][col] = 0
            else:
                new_pixels[col,row] = pixels[col,row]
                
    image = new_image
    pixels = image.load()

    

    
    

    #Otsu's Method-----------------------------------------------------------------------------------------------
    #This will find the upper bound and the lower bound is typically set to half the upper
    
    int_grad = gradients.astype(int)
    histogram = [np.count_nonzero(int_grad == i) for i in range(np.amax(int_grad))]
    
    top = 0
    best_ob = 0
    for t in range(len(histogram)-1):
        wb = sum(histogram[:t+1])/(image.size[0]*image.size[1])
        wf = sum(histogram[t+1:])/(image.size[0]*image.size[1])

        if wb == 0 or wf == 0:
            continue
        
        ub = sum([histogram[i]*i for i in range(t+1)]) / sum(histogram[:t+1])
        uf = sum([histogram[i]*i for i in range(t+1, len(histogram))]) / sum(histogram[t+1:])
        
        ob = wb*wf*(ub-uf)**2
        
        if ob > best_ob:
            top = t+1
            best_ob = ob


    top -= 50
    bottom = top//2
    
    print(top)
    #Hysteresis Thresholding-------------------------------------------------------------------------------------
    """
    Otsu's Method is used to find the max/min range

    1. Set a min and max range
    2. Anything below min is discarded and everything above max is kept and labeled as "strong"
    3. Anything in the middle must be connected to a strong pixel (at least 1 of its 8 neighbors is a strong pixel)
    
    """
    for col in range(image.size[0]):
        for row in range(image.size[1]):
            
            if gradients[row][col] < bottom:
                pixels[col,row] = 0
            elif gradients[row][col] < top:
                directions = [[0, 1], [1, 1], [1, 0], [-1, 1], [-1, 0], [-1, -1], [-1, 0], [1, -1]]
                connected = False

                for d in directions:
                    if 0 <= row+d[0] < image.size[1] and 0 <= col+d[1] < image.size[0] and gradients[row+d[0]][col+d[1]] > top:
                        break
                        connected = True
                
                if connected:
                    pixels[col, row] = 255
                else:
                    pixels[col,row] = 0
            else:
                pixels[col,row] = 255



    return image


def trace_gif(gif_path):
    frames = []
    count = 1
    gif = imageio.get_reader(gif_path)
    
    for frame in gif:
        frames.append(trace_image(Image.fromarray(frame)))
        print("Frame {0}/{1} completed...".format(count, len(gif)))
        count += 1

    imageio.mimsave(r"C:\Users\Peanu\OneDrive\Desktop\{0}.gif".format(random.randint(0, 2**31-1)), frames, duration=(1/24))
    
        

trace_image(Image.open(r"C:\Users\Peanu\OneDrive\Desktop\UncannyEdgeDetection\renei.jpg")).show()
    






















        

