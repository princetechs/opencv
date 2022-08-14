import cv2
# cv2 for image show

# print("hello opencv")
# image=cv2.imread("firstday/opencvtest.jpeg")
# cv2.imshow("Output",image)
# cv2.waitKey(0)

# show gray image 

print("hello opencv")
image=cv2.imread("firstday/opencvtest.jpeg")
# print(image.shape)
imcrop=image[0:200,200:500]
# imgray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# imblur=cv2.GaussianBlur(imgray,(7,7),0)
imresiz=cv2.resize(image,(100,100))
# imcanny=cv2.Canny(image,150,200)
# imdialate=cv2.dilate(imcanny,)

# cv2.imshow("gray image",imgray)
cv2.imshow("blur image",imcrop)

cv2.waitKey(1000)