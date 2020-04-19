
# importing opencv 
import cv2 
  
# Load our input image 
image = cv2.imread('img/tomatoes.png') 
cv2.imshow('Original', image) 
#cv2.waitKey() 
  
# We use cvtColor, to convert to grayscale 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0)   
  
# window shown waits for any key pressing event 
cv2.destroyAllWindows() 
