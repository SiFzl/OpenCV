# import cv2
# import numpy as np

# # Read the image and convert it to grayscale
# image = cv2.imread("/Users/sina.fazel/Desktop/Python/Project/test2-3.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply Gaussian Blur to reduce noise
# blur = cv2.GaussianBlur(gray, (5,5), 0)

# # Apply thresholding to create a binary image
# _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)

# # Find contours on the binary image
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Filter out the smaller contours (to remove noise)
# contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]

# # Sort the contours from left to right (to determine the order of gates)
# contours = sorted(contours, key=lambda cnt: cv2.boundingRect(cnt)[0])

# # Draw contours around the gates
# image_contours = image.copy()
# for cnt in contours:
#     x,y,w,h = cv2.boundingRect(cnt)
#     cv2.rectangle(image_contours, (x,y), (x+w,y+h), (0,0,255), 2)

# # Calculate the centers of each gate
# centers = []
# for cnt in contours:
#     M = cv2.moments(cnt)
#     center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
#     centers.append(center)

# # Determine which center corresponds to the first gate and which one corresponds to the last gate
# centers = sorted(centers, key=lambda c: c[0])
# first_gate_center = centers[0]
# last_gate_center = centers[-1]

# # Display the results
# cv2.imshow("Image", image)
# cv2.imshow("Contours", image_contours)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




import cv2
import numpy as np

# Load image
img = cv2.imread('/Users/sina.fazel/Desktop/Python/Project/test2-3.jpg')

# Convert image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for red-purple color
lower = np.array([140, 50, 50])
upper = np.array([180, 255, 255])

# Threshold the image to obtain only red-purple colors
mask = cv2.inRange(hsv, lower, upper)

# Find contours in the mask image
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours around gates
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# Find centers of gates
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



