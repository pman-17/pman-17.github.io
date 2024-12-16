import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    blur = np.ones((10, 10), np.float32)/30

    outline = np.array([[-1, -1, -1], 
                    [-1, 8, -1], 
                    [-1, -1, -1]]) 
    
    frame = cv2.filter2D(src=frame, ddepth=-1, kernel=outline) 

    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == "q":
        break

cap.release()
cv2.destroyAllWindows()