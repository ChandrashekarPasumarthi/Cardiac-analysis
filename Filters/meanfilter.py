import cv2
import numpy as np
import argparse
 
# create the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to the input image')
args = vars(ap.parse_args())
print(args['image'])
print(type(args['image']))
# read the image

image = cv2.imread(args['image'],0)
print(image.shape)
cv2.imshow('Org image', image)
# apply the 3x3 mean filter on the image
kernel = np.ones((3,3),np.float32)/9
processed_image = cv2.filter2D(image,-1,kernel)
# display image
cv2.imshow('Mean Filter Processing', processed_image)
# save image to disk
cv2.imwrite('/home/chandra/Documents/Heart/Filters/MeanFilter/processed_image.png', processed_image)
# pause the execution of the script until a key on the keyboard is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
