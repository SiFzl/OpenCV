import cv2
import numpy as np

# Load image
img = cv2.imread('/Users/sina.fazel/Desktop/Python/Project/test1-2.png')

# Convert image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define lower and upper range of orange color in HSV
lower_orange = np.array([10, 100, 20])
upper_orange = np.array([25, 255, 255])

# Threshold the image to get only orange regions
mask = cv2.inRange(hsv, lower_orange, upper_orange)

# Apply a Gaussian blur to reduce noise
blur = cv2.GaussianBlur(mask, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blur, 50, 150, apertureSize=3)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort the contours by area
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Find the largest rectangular contour
largest_contour = None
for contour in contours:

    polygon = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
 # Check if the polygon (Chand Zelei) has four vertices (Raas) (Like a rectangle)
    if len(polygon) == 4:
        largest_contour = polygon
        break

# Draw a circle around the center of the rectangular contour
if largest_contour is not None:
    M = cv2.moments(largest_contour)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    cv2.circle(img, center, 5, (0, 0, 255), -1)

# Draw the contour on the original image
cv2.drawContours(img, [largest_contour], 0, (0, 255, 0), 3)

# Show the result
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
