import cv2
image=cv2.imread('img.jpg',1)
# print(image)
cv2.imshow('image',image)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('img.png',image)