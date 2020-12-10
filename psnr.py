from math import log10, sqrt 
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
from skimage import color, data, restoration

  
def PSNR(original, compressed): 
    mse = np.mean((original - compressed) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr 


f = open("PSNR_values.txt", "w") 

for k in range(1,34):
	#Grey Images
		image = cv.imread(r'/home/chandra/Documents/Heart/Grey_images/pat'+str(k)+'_1_1gray.jpg',0)
	#mean filter images
		mean_image=cv.imread(r'/home/chandra/Documents/Heart/Filters/MeanFilter/mean_image'+str(k)+'.jpg',0)
		psnr_mean=PSNR(image,mean_image)
		f.write('psnr mean of pat'+str(k)+' '+str(psnr_mean)+'\n')
	#Gaussian Blur
		Gaussian_image=cv.imread(r'/home/chandra/Documents/Heart/Filters/GaussianFilter/gaussian_image'+str(k)+'.jpg',0)
		psnr_gaussian=PSNR(image,Gaussian_image)
		f.write('psnr gaussian of pat'+str(k)+' '+str(psnr_gaussian)+'\n')
	#Median Blur
		Median_image=cv.imread(r'/home/chandra/Documents/Heart/Filters/MedianFilter/median_image'+str(k)+'.jpg',0)
		psnr_median=PSNR(image,Median_image)
		f.write('psnr median of pat'+str(k)+' '+str(psnr_median)+'\n')
	#Wiener Filter
		Wiener_image=cv.imread(r'/home/chandra/Documents/Heart/Filters/WienerFilter/wiener_image'+str(k)+'.jpg',0)
		psnr_wiener=PSNR(image,Wiener_image)
		f.write('psnr wiener of pat'+str(k)+' '+str(psnr_wiener)+'\n')
		f.write("\n")
f.close()


