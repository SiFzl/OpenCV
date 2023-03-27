import cv2
import numpy as np

# Load image
img = cv2.imread('/Users/sina.fazel/Desktop/Python/Project/test1-2.png')

# Convert image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range of orange color in HSV
lower_orange = np.array([0, 50, 50])
upper_orange = np.array([20, 255, 255])

# Threshold the image to get only orange colors
mask = cv2.inRange(hsv, lower_orange, upper_orange)

# Find contours in the thresholded image
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area, in descending order
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Find the center of the largest contour (i.e. the orange rectangle)
if contours:
    rect = cv2.minAreaRect(contours[0])
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    center = np.mean(box, axis=0, dtype=np.int0)

    # Draw a circle at the center of the orange rectangle
    cv2.circle(img, tuple(center), 5, (0, 255, 0), -1)

    # Draw a corresponding contour around the orange rectangle
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# Display output image
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

