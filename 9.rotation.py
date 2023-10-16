import cv2

path = r"//Mac/Home/Documents/sample9.png"
src = cv2.imread(path)

window_name = 'Image'
rotate = int(input("Enter 1 for 180-degree rotation or 2 for 90-degree rotation: "))

if rotate == 1:
    image = cv2.rotate(src, cv2.ROTATE_180)
elif rotate == 2:
    image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
else:
    print("Invalid input")

if image is not None:
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
