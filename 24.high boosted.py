import cv2
import numpy as np

image = cv2.imread("//Mac/Home/Pictures/sampleimg1.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
A = 1  

laplacian_mask = np.array([[0, -1, 0],
                           [-1, A + 4, -1],
                           [0, -1, 0]], dtype=np.float32)

sharpened_image = cv2.filter2D(gray_image, -1, laplacian_mask)


sharpened_image = cv2.addWeighted(gray_image, 1 + A, sharpened_image, -A, 0)

sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)

cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('sharpened_image.jpg', sharpened_image)
