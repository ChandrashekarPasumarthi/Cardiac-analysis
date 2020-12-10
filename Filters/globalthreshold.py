import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time
from skimage import restoration
for k in range(1,34):
  img = cv.imread('/home/chandra/Documents/Heart/Grey_images/pat'+str(k)+'_1_1gray.jpg',0)
# global thresholding
  ret1,th1 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding
  kernel = np.ones((3,3),np.float32)/9
  mean = cv.filter2D(img,-1,kernel)
#img1 = cv.imread('/home/chandra/Documents/Heart/Filters/Mean Filter/processed_image.jpg',0)
  ret2,th2 = cv.threshold(mean,0,1,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
  gauss = cv.GaussianBlur(img,(5,5),0)
  ret3,th3 = cv.threshold(gauss,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#median filter
  median = cv.medianBlur(img,9)
  ret4,th4 = cv.threshold(median,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#wiener filter
  psf = np.ones((5,5)) / 25
  wiener = restoration.wiener(img,psf,1100) 
  ret5,th5 = cv.threshold(wiener,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
  #ret5,th5 = adaptiveThreshold(wiener, 0, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 75, 10);

# plot all the images and their histograms
  images = [img, th1,
          mean, th2,
          gauss, th3,
          median, th4,
          wiener, th5]
  titles = ['Original Image'+str(k),'Global Thresholding'+" "+str(ret1),
          'Mean filtered Image',"Otsu's Thresholding"+" "+str(ret2),
          'Gaussian filtered Image',"Otsu's Thresholding"+" "+str(ret3),
          'Median filtered Image',"Otsu's Thresholding"+" "+str(ret4),
          'Wiener filtered Image',"Otsu's Thresholding"+" "+str(ret5)]
  for i in range(5):
    plt.subplot(5,2,i*2+1),plt.imshow(images[i*2],'gray')
    plt.title(titles[i*2]), plt.xticks([]), plt.yticks([])

    plt.subplot(5,2,i*2+2),plt.imshow(images[i*2+1],'gray')
    plt.title(titles[i*2+1]), plt.xticks([]), plt.yticks([])
    
    #plt.savefig('/home/chandra/Documents/Heart/Filters/Thresholds/pat'+str(k)+'.jpg')
  plt.show()

#time.sleep(1)

