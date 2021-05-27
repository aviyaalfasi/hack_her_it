import cv2
import time
from plyer import notification # for getting notification on your PC


def popup_message(accept_title, accept_message):
    notification.notify(
            # title of the notification,
            title=accept_title,
            # the body of the notification
            message=accept_message,
            # creating icon for the notification
            # we need to download a icon of ico file format
            app_icon=None,

            # the notification stays for 50sec
            timeout=50
        )


def get_face_sizes(picture):
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
    max_sizes = {'max_face_size': max_face_size, 'x': 0, 'y': 0, 'w': 0, 'h': 0}
    for (x, y, w, h) in faces:
        face_size = h
        if face_size > max_sizes['max_face_size']:
            max_sizes['max_face_size'] = face_size
            max_sizes['x'] = x
            max_sizes['y'] = y
            max_sizes['w'] = w
            max_sizes['h'] = h

    return max_sizes


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


def run():
    count_difference = 0
    TRESHHOLD = 10
    MAX_DIFFERENCES_AMOUNT = 2
    SECONDS_TO_SLEEP = 2

    picture_number = 0

    initial_picture = take_picture()
    # cv2.imshow("preview", initial_picture)
    initial_picture_face_size = get_face_sizes(initial_picture)
    cv2.rectangle(initial_picture, (initial_picture_face_size['x'], initial_picture_face_size['y']), (
    initial_picture_face_size['x'] + initial_picture_face_size['w'],
    initial_picture_face_size['y'] + initial_picture_face_size['h']), (0, 255, 0), 2)
    cv2.imwrite('height_test\initial_picture.jpg', initial_picture)

    while True:
        picture_number += 1
        current_picture = take_picture()
        current_picture_face_size = get_face_sizes(current_picture)
        cv2.rectangle(current_picture, (current_picture_face_size['x'], current_picture_face_size['y']), (current_picture_face_size['x'] + current_picture_face_size['w'], current_picture_face_size['y'] + current_picture_face_size['h']), (0, 255, 0), 2)
        cv2.imwrite('height_test\\' + str(picture_number) + '.jpg', current_picture)

        if abs(current_picture_face_size['max_face_size'] - initial_picture_face_size['max_face_size']) > TRESHHOLD:
            count_difference += 1
        else:
            count_difference = 0

        if count_difference >= MAX_DIFFERENCES_AMOUNT:
            print('Problem')
            count_difference = 0
        # take a picture every 5 seconds
        time.sleep(SECONDS_TO_SLEEP)


run()



