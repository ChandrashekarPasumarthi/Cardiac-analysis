import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
for k in range(1,34):
	image = cv.imread(r'/home/chandra/Documents/Heart/Grey_images/pat'+str(k)+'_1_1gray.jpg',0)
	ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
	kernel = np.ones((3,3),np.float32)/9
	mean_image= cv.filter2D(image,-1,kernel)
	cv.imwrite('/home/chandra/Documents/Heart/Filters/MeanFilter/mean_image'+str(k)+'.jpg',mean_image)
	gaussian_image = cv.GaussianBlur(image,(5,5),0)
	cv.imwrite('/home/chandra/Documents/Heart/Filters/GaussianFilter/gaussian_image'+str(k)+'.jpg',gaussian_image)
	new_image = cv.medianBlur(image,9)
	cv.imwrite('/home/chandra/Documents/Heart/Filters/MedianFilter/median_image'+str(k)+'.jpg',new_image)
