import cv2
import numpy as np

# Load image
img = cv2.imread("/Users/sina.fazel/Desktop/Python/Project/test2-1.png")

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for red color
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

# Create a mask for red color
mask_red1 = cv2.inRange(hsv, lower_red, upper_red)
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask_red = mask_red1 + mask_red2

# Find contours in the mask
contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours and mark centers
centers = []
for cnt in contours:
    # Find the bounding rectangle of each contour
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 10 and h > 10:
        # Draw the contour and a circle at its center
        cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
        center = (int(x + w/2), int(y + h/2))
        cv2.circle(img, center, 3, (0, 0, 255), -1)
        centers.append(center)

# Sort centers from left to right
centers.sort(key=lambda c: c[0])

# Print the first and last centers
print("First center:", centers[0])
print("Last center:", centers[-1])

# Show the output image
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



