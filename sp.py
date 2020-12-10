import cv2
import numpy as np
import random

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('/home/chandra/Documents/Heart/Grey_images/pat33_1_1gray.jpg',0) # Only for grayscale image
noise_img = sp_noise(image,0.05)
cv2.imwrite('/home/chandra/Documents/Heart/S&P_images/pat33_1_1.jpg', noise_img)