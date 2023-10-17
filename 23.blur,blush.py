import cv2
import numpy as np

image = cv2.imread("//Mac/Home/Pictures/sampleimg1.png")


blurred_image = cv2.GaussianBlur(image, (0, 0), 3)

unsharp_mask = cv2.addWeighted(image, 2.5, blurred_image, -1.5, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Unsharp Masked Image', unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
