import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import color, data, restoration
for k in range(1,34):
	image = cv.imread(r'/home/chandra/Documents/Heart/Grey_images/pat'+str(k)+'_1_1gray.jpg',0)
	kernel = np.ones((3,3),np.float32)/9
	mean_image= cv.filter2D(image,-1,kernel)
	cv.imwrite('/home/chandra/Documents/Heart/Filters/MeanFilter/mean_image'+str(k)+'.jpg',mean_image)
	gaussian_image = cv.GaussianBlur(image,(5,5),0)
	cv.imwrite('/home/chandra/Documents/Heart/Filters/GaussianFilter/gaussian_image'+str(k)+'.jpg',gaussian_image)
	new_image = cv.medianBlur(image,9)
	cv.imwrite('/home/chandra/Documents/Heart/Filters/MedianFilter/median_image'+str(k)+'.jpg',new_image)
	psf = np.ones((5,5)) / 25
	Wiener_filtered = restoration.wiener(image,psf,1100) 
	cv.imwrite('/home/chandra/Documents/Heart/Filters/WienerFilter/wiener_image'+str(k)+'.jpg',new_image)
