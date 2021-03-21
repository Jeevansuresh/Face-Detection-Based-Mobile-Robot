import cv2
import time 
import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
# Load the cascade

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)


while True:
    # Read the frame
    _, img = cap.read()

    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        GPIO.output(5,True)
        time.sleep(1)
        GPIO.output(5,False)
        time.sleep(1)
        GPIO.output(5,True)
        time.sleep(1)
        #place the robot with no faces seen then  let the robot make a complete 360 without faces visible to it and by trial and error add this again and again


        

    
    cv2.imshow('img', img)
    GPIO.output(5,False)
    GPIO.output(13,False)
    GPIO.output(4,True)
    GPIO.output(6,True)

cap.release()
