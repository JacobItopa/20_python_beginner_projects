import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("Human_faces.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, l) in face:
    cv2.rectangle(img,(x, y), (x+w, y+l), (250,0,2), 2)

cv2.imshow("img", img)
cv2.waitKey()

cv2.imwrite("face_detection.jpg", img)