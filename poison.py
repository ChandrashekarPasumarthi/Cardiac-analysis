from skimage.util import random_noise
import cv2

img = cv2.imread('/home/chandra/Documents/Heart/Grey_images/pat1_1_1gray.jpg',0) # Only for grayscale image


noisy = random_noise(img, mode="poisson")
cv2.imwrite('/home/chandra/Documents/Heart/Poison_images/pat1_1_1.jpg', noisy)
