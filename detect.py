import cv2
import numpy as np
# read the image 
img = cv2.read("img.jpg")

# since the colors in the image is in RGB formt convert it into HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# suppose we want to detect the blue color
# provide the lower and upper range of blue color

lower_range = np.array([10,50,50])
upper_range = np.array([130,255,255])

# create mask
mask = cv2.inRange(hsv, lower_range, upper_range)
cv2.imgShow("Image", img)
cv2.imgShow("Maks", mask)

# display the window infinitly until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindow()
