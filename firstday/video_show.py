from sre_constants import SUCCESS
import cv2

#show video using open cv

# print("video_show")
# cap=cv2.VideoCapture("firstday/sample-mp4-file-small.mp4")
# while True:
#     success,img=cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


# show video live by camera

print("video_show")
cap=cv2.VideoCapture(0)
cap.set(3,200)
cap.set(4,200)
cap.set(10,100)
while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break