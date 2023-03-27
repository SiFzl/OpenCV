import cv2
import numpy as np

# Load image
img = cv2.imread('/Users/sina.fazel/Desktop/Python/Project/test2-3.jpg')

# Convert image to HSV 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for red-purple color
lower = np.array([140, 50, 50])
upper = np.array([180, 255, 255])

# Threshold the image for only red-purple colors
mask = cv2.inRange(hsv, lower, upper)

# Apply a Gaussian blur to reduce noise
blur = cv2.GaussianBlur(mask, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blur, 50, 150, apertureSize=3)

# Find contours in the mask image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours around the gates
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# Find centers of the gates
centers = []
for cnt in contours:
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        centers.append(center)
        
# Find first and last gate
first_gate_center = centers[0]
last_gate_center = centers[0]
for center in centers:
    if center[1] < first_gate_center[1]:
        first_gate_center = center
    if center[1] > last_gate_center[1]:
        last_gate_center = center

# Draw circles around center of first and last gates
img_centers = img_contours.copy()
cv2.circle(img_centers, first_gate_center, 5, (0, 0, 255), -1)
cv2.circle(img_centers, last_gate_center, 5, (0, 0, 255), -1)

# Show images
cv2.imshow('Original Image', img)
cv2.imshow('Contours Around Gates', img_contours)
cv2.imshow('Gate Centers', img_centers)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print first and last gate centers
print("First gate center: ", first_gate_center)
print("Last gate center: ", last_gate_center)



