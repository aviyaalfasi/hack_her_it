import cv2
import time
from plyer import notification # for getting notification on your PC
from argonomic import vidoe_camera


def popup_message(accept_title, accept_message):
    notification.notify(
            # title of the notification,
            title=accept_title,
            # the body of the notification
            message=accept_message,
            # creating icon for the notification
            # we need to download a icon of ico file format
            app_icon=r'logo\note1.ico',

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
    max_sizes = {'max_face_size': max_face_size, 'x': 0, 'y': 0, 'width': 0, 'height': 0}
    for (x, y, width, height) in faces:
        face_size = width * height
        if face_size > max_sizes['max_face_size']:
            max_sizes['max_face_size'] = face_size
            max_sizes['x'] = x
            max_sizes['y'] = y
            max_sizes['width'] = width
            max_sizes['height'] = height

    return max_sizes


def take_picture(cap, click_required=False):
    # Open the device at the ID 0
    # Use the camera ID based on
    # /dev/videoID needed

    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    print("Taking picture...")

    # if needed, wait for click from user
    if click_required:
        cv2.imshow("AppRight", frame)
        keyboard_click = -1
        while keyboard_click not in [ord('a'),10]:
            keyboard_click = cv2.waitKey(2)
            # max_face = get_face_sizes(frame)
            # cv2.rectangle(frame, (max_face['x'], max_face['y']), (
            #     max_face['x'] + max_face['width'],
            #     max_face['y'] + max_face['height']), (0, 255, 0), 2)
            # cv2.imshow("AppRight", frame)
    return frame


def restart_app(threshold=30, seconds_to_sleep=2, max_differences=2):
    count_difference = 0
    picture_number = 0

    # waiting for user clicking

    # initial_picture = take_picture(click_required=True)
    initial_picture = vidoe_camera.show_video()
    print("********  You are all set!  ********")
    # cv2.imshow("preview", initial_picture)
    initial_picture_face_size = get_face_sizes(initial_picture)
    cv2.rectangle(initial_picture, (initial_picture_face_size['x'], initial_picture_face_size['y']), (
    initial_picture_face_size['x'] + initial_picture_face_size['width'],
    initial_picture_face_size['y'] + initial_picture_face_size['height']), (0, 255, 0), 2)
    cv2.imwrite('height_test\initial_picture.jpg', initial_picture)

    cap = cv2.VideoCapture(0)
    # Check if camera was opened correctly
    if not (cap.isOpened()):
        print("Could not open video device")
        exit()
    print("Camera opened successfully")

    while True:
        picture_number += 1
        current_picture = take_picture(cap)
        current_picture_face_size = get_face_sizes(current_picture)
        # cv2.rectangle(current_picture, (current_picture_face_size['x'], current_picture_face_size['y']), (current_picture_face_size['x'] + current_picture_face_size['width'], current_picture_face_size['y'] + current_picture_face_size['height']), (0, 255, 0), 2)
        # cv2.imwrite('height_test\\' + str(picture_number) + '.jpg', current_picture)

        if current_picture_face_size['height'] - initial_picture_face_size['height'] > threshold:
            count_difference += 1
        else:
            count_difference = 0

        if count_difference >= max_differences:
            print('********  Problem!!!  ********')
            popup_message("AppRight", "Reminder:\nSit healthy")
            # return False
            count_difference = 0
        # take a picture every 5 seconds
        time.sleep(seconds_to_sleep)

    cap.release()
    cv2.destroyAllWindows()

#
# def run():
#     is_stable = restart_app()
#     while True:
#         restart_app()

restart_app()
