import cv2
import numpy as np

img = cv2.imread('temp_page.png', cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY_INV)

# Find connected components or contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

h, w = img.shape

# The caption is around y=202 to 214.
# Let's find contours above or containing this area.
fig_contours = []
for cnt in contours:
    x, y, cw, ch = cv2.boundingRect(cnt)
    # Filter out very small noise
    if cw * ch < 100:
        continue
    print(f"Contour: x={x}, y={y}, w={cw}, h={ch}, norm: x1={x/w:.4f}, y1={y/h:.4f}, x2={(x+cw)/w:.4f}, y2={(y+ch)/h:.4f}")
