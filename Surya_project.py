import cv2
cam=cv2.VideoCapture(0)

a,img=cam.read()
loc="/tmp/Screenshot"
ext='.png'

for i in range(10):
	a=str(i)
	cv2.imwrite(loc+a+ext,img)

cam.release()

