import cv2
import time


def get_face_size(picture):
    """
    :param picture: a picture
    :return: the size of the person in the picture 'picture'
    """
    gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    max_face_size = 0
    for (x, y, w, h) in faces:
        face_size = w * h
        if face_size > max_face_size:
            max_face_size = face_size
    return max_face_size


def take_picture():
    # Open the device at the ID 0
    # Use the camera ID based on
    # /dev/videoID needed
    cap = cv2.VideoCapture(0)

    # Check if camera was opened correctly
    if not (cap.isOpened()):
        print("Could not open video device")

    # Set the resolution

    ret, frame = cap.read()
    cap.release()
    return frame


count_difference = 0
threshold = 100
picture_number = 0

initial_picture = take_picture()
initial_picture_face_size = get_face_size(initial_picture)
cv2.imwrite('height_test\initial_picture.jpg', initial_picture)

while True:
    picture_number += 1
    current_picture = take_picture()
    current_picture_face_size = get_face_size(current_picture)
    cv2.imwrite('height_test\\' + str(picture_number) + '.jpg', current_picture)
    if abs(current_picture_face_size - initial_picture_face_size) > threshold:
        count_difference += 1
    if count_difference >= 2:
        print('Problem')
        count_difference = 0
    time.sleep(5)








