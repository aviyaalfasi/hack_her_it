# only live feed showing , capture Image (c), start video recording (v), pause video recording (p)
# resume video recording (r), stop video recording (b), exit program (q)
# to stop recording and exit (q)
import cv2
# from datetime import datetime


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

#
# if (cap.isOpened()):
# 	show_video()
# else:
# 	cap.open()
# 	show_video()
#
# cap.release()
# cv2.destroyAllWindows()
