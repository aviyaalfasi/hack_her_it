import cv2
import sys

#imagePath = r'C:\Users\osnat\Documents\people_with_phones.png'
imagePath = r'C:\Users\osnat\PycharmProjects\hack_her_it\argonomic\height_test\1.jpg'
#imagePath = r'2.jpg'
#imagePath = r'3.jpg'
basic_W = 513
basic_H = 513

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

print("[INFO] Found {0} Faces.".format(len(faces)))
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    cv2.imwrite(str(w) + str(h) + r'C:\Users\osnat\PycharmProjects\hack_her_it\argonomic\height_test\_faces.jpg', roi_color)
    if basic_W * basic_H > w * h:
        print('smaller')
    else:
        print('bigger')

status = cv2.imwrite(r'C:\Users\osnat\PycharmProjects\hack_her_it\argonomic\height_test\faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)