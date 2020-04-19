
import cv2 
import numpy as np 
import matplotlib.pyplot as plt  
# % matplotlib qt 
# This is a magic command to display in external window 
  
image = cv2.imread("img/tomatoes.png")
# plt.subplot(2, 2, 1)
# plt.title("Tomatoes") 
# plt.imshow(image)
# plt.show()

# Loading the image 
  
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1) 
bigger = cv2.resize(image, (1050, 1610)) 
  
stretch_near = cv2.resize(image, (780, 540),  
               interpolation = cv2.INTER_NEAREST) 
  
  
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"] 
images =[image, half, bigger, stretch_near] 
count = 4
  
for i in range(count): 
    plt.subplot(2, 2, i + 1) 
    plt.title(Titles[i]) 
    plt.imshow(images[i]) 
  
plt.show() 
