import cv2
import numpy as np

# read the image
img = cv2.imread('/Users/sina.fazel/Desktop/Python/Project/test1-1.png')

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply threshold to get binary image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# find the largest contour
largest_contour = max(contours, key=cv2.contourArea)

# draw the largest contour
cv2.drawContours(img, [largest_contour], 0, (0, 255, 0), 3)

# find the moments of the largest contour
M = cv2.moments(largest_contour)

# calculate the center of the contour
center_x = int(M['m10']/M['m00'])
center_y = int(M['m01']/M['m00'])

# draw a circle at the center of the contour
cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)

# display the output image
cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
