import cv2
import numpy as np

# Load test image
img = cv2.imread("test.jpg")
if img is None:
    print("Image not found")
    exit()

# Resize for speed
img = cv2.resize(img, (640, 480))

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Green color range (adjust later)
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

# Mask green areas
mask = cv2.inRange(hsv, lower_green, upper_green)

# Clean noise
kernel = np.ones((5,5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Find contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    if cv2.contourArea(c) > 500:  # filter small noise
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# Show result
cv2.imshow("Detected Plants", img)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()