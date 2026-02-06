import cv2
import numpy as np

# Create blank soil background (brown)
height, width = 480, 640
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:] = (42, 42, 165)  # brown soil (BGR)

# Draw crop rows (green vertical rectangles)
row_x_positions = [150, 320, 490]
for x in row_x_positions:
    cv2.rectangle(image, (x-20, 0), (x+20, height), (0, 255, 0), -1)

# Draw weeds (random green circles between rows)
np.random.seed(0)
for _ in range(15):
    x = np.random.randint(0, width)
    y = np.random.randint(0, height)

    # Skip if near crop rows
    if any(abs(x - row) < 40 for row in row_x_positions):
        continue

    radius = np.random.randint(5, 15)
    cv2.circle(image, (x, y), radius, (0, 200, 0), -1)

cv2.imshow("Synthetic Field", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
