import cv2
import time
from plyer import notification # for getting notification on your PC
#from argonomic import vidoe_camera
import tkinter
from tkinter.ttk import *
import PIL.Image, PIL.ImageTk
import threading

gt = None

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

def start_process():
	cap = cv2.VideoCapture(0)
	cv2.namedWindow('AppRight', cv2.WINDOW_NORMAL)
	return cap


def show_video():
	cap = start_process()
	global recordControl
	while True:
		# now = datetime.now()
		# time = datetime.time(now)
		# name = "capture_" + now.strftime("%y%m%d") + time.strftime("%H%M%S") + ".jpg"
		ret, frame = cap.read()
		if ret is True:
			frame = cv2.flip(frame, 1)   # 1 = vertical , 0 = horizontal

			cv2.imshow('AppRight', frame)

			k = cv2.waitKey(1) & 0Xff
			if k == ord('q'):  # Quit program and recording
				cap.release()
				cv2.destroyAllWindows()
				break
			elif k in [32, 13]:  # capture Image, captures image when the user clicks on whitespace (32) or enter (13)
				cap.release()
				cv2.destroyAllWindows()
				return frame
		else:
			break


class App:
    def __init__(self, window, window_title, image_path="logo\logo15.jpg"):
        self.window = window
        self.window.title(window_title)
        self.is_closed = True

        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        #self.cv_img = cv2.Canny(, 50, 100)640w, 480h

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

         # Button that lets the user blur the image
        self.btn_blur=tkinter.Button(window, text="Start", width=50, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)

        self.window.mainloop()

    # Callback for the "Blur" button
    def blur_image(self):
         # self.cv_img = cv2.blur(self.cv_img, (3, 3))
         # self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
         # self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.destroy()
        self.is_closed = False
        # Calibration(tkinter.Tk(), "Appright")

class Window(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        self.window = tkinter.Tk()
        self.window.title("Appright")


        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread("logo\logo15.jpg"), cv2.COLOR_BGR2RGB)
        #self.cv_img = cv2.Canny(, 50, 100)640w, 480h

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(self.window, width = self.width, height = self.height)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

         # Button that lets the user blur the image
        self.btn_blur=tkinter.Button(self.window, text="restart picture", width=50, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)

        self.window.mainloop()

    # Callback for the "Blur" button
    def blur_image(self):
         # self.cv_img = cv2.blur(self.cv_img, (3, 3))
         # self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
         # self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.destroy()
        Calibration(tkinter.Tk(), "Appright")
        # Calibration(tkinter.Tk(), "Appright")


class Calibration:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.is_colse = True

        #p1 = PhotoImage(file='logo.jpg')

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            #cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            self.vid.__del__()
            self.canvas.destroy()
            self.window.destroy()
            #App(tkinter.Tk(), "Appright")
            global gt
            gt = frame
            self.is_colse = False
            Window()
            #return frame

    def update(self):
        # Get a frame from the video source
       ret, frame = self.vid.get_frame()

       if ret:
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

       self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            popup_message("Fialed", "unable to open video source")
            return

         # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (None, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


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


def restart_app(threshold=30, seconds_to_sleep=3, max_differences=2):
    count_difference = 0
    picture_number = 0

    # waiting for user clicking

    # initial_picture = take_picture(click_required=True)
    app = App(tkinter.Tk(), "Appright")
    if app.is_closed:
        return
    calibration = Calibration(tkinter.Tk(), "Appright")
    if calibration.is_colse:
        return
    initial_picture =  gt# show_video() #App(tkinter.Tk(), "Appright")vidoe_camera.
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

#App(tkinter.Tk(), "Appright")
restart_app()

# App(tkinter.Tk(), "Appright")