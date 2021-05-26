import cv2


def get_person_size(picture):
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
    max_person_size = 0
    for (x, y, w, h) in faces:
        person_size = w * h
        if person_size > max_person_size:
            max_person_size = person_size
    return max_person_size

