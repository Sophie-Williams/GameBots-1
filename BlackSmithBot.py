import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey , ReleaseKey , W , A , S , D

for i in list(range(4))[::-1]:
	print i+1
	time.sleep(1)

def process_img(original_image):
	processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img,threshold1=200,threshold2=300)
	return processed_img
	
	
last_time = time.time()
while(True):
	screen = np.array(ImageGrab.grab(bbox=(0,40,640,480)))
	cv2.rectangle(screen,(190,255),(200,270),(255,0,0),2)
	#new_screen = process_img(screen)
	pixel= screen[260, 195]
	
	if pixel[0]==217:
		PressKey(A)
		ReleaseKey(A)
		time.sleep(0.25)
	elif pixel[0]==33:
		PressKey(D)
		ReleaseKey(D)
		time.sleep(0.25)
	#print('Loop took {} seconds'.format(time.time()-last_time))
	last_time = time.time()
	#cv2.imshow('window',screen)
	cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break