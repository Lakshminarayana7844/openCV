import cv2
import numpy as np

image = cv2.imread("//Mac/Home/Pictures/sampleimg1.png")

laplacian_mask = np.array([[1, 1, 1],
                           [1, -8, 1],
                           [1, 1, 1]], dtype=np.float32)

sharpened_image = cv2.filter2D(image, -1, laplacian_mask)

sharpened_image = cv2.add(image, sharpened_image)

cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('sharpened_image.jpg', sharpened_image)
