import cv2
image=cv2.imread('img.jpg',1)
cv2.line(image,(0,0),(200,200),(255,0,255),4)
cv2.rectangle(image,(0,0),(200,200),(0,255,0),4)
cv2.circle(image,(500,50),50,(0,0,255),-1)
font=cv2.FONT_ITALIC
cv2.putText(image,"niyan",(200,100),font,3,(255,255,255),cv2.LINE_AA)
cv2.imshow("shapes",image)
cv2.waitKey(0)
cv2.destroyAllWindows()