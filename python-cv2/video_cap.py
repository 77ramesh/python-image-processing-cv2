import cv2
import numpy as np

video = cv2.VideoCapture(0)

#will run for infinite until pressed q
while True:
    ret, frame = video.read()
    
    #making video gray scale
    #opencv works in format BGR unlike any other library or any inbuilt functions-
    #in any programming language
    #in others if you want red, the code is RGB ie. (255, 0, 0)
    #in opencv BGR (0, 0, 255)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Video Capturing", frame)
    cv2.imshow("Video Capturing: gray", gray)
    
    #will break while loop and exit video capturing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
