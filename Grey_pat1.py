import cv2
  
image = cv2.imread(r'/home/chandra/Documents/mri_images/patient33/1_1.jpg')
print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape)
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
cv2.imwrite('/home/chandra/Documents/Heart/Grey_images/pat33_1_1gray.jpg',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
