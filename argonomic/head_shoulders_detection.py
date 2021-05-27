import cv2
cap=cv2.VideoCapture(0)

ret1,frame1= cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (25, 25), 0)
cv2.imshow('window',frame1)

while(True):
    ret2,frame2=cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    deltaframe=cv2.absdiff(gray1,gray2)
    cv2.imshow('delta',deltaframe)