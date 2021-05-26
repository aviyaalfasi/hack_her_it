import time

import cv2

from argonomic import get_first_picture

count_difference = 0
threshold = 100
picture_number = 0

initial_picture = get_first_picture.take_picture()
initial_picture_size = get_first_picture.get_person_size(initial_picture)
cv2.imwrite('initial_picture.jpg', initial_picture)

while True:
    picture_number += 1
    current_picture = get_first_picture.take_picture()
    current_picture_size = get_first_picture.get_person_size(current_picture)
    cv2.imwrite(str(picture_number) + '.jpg', current_picture)
    if abs(current_picture_size - initial_picture_size) > threshold:
        count_difference += 1
    if count_difference >= 2:
        print('Problem')
        count_difference = 0
    time.sleep(5)






